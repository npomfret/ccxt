# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import hashlib
import math
from ccxt.base.errors import ExchangeError


class btcturk(Exchange):

    def describe(self):
        return self.deep_extend(super(btcturk, self).describe(), {
            'id': 'btcturk',
            'name': 'BTCTurk',
            'countries': ['TR'],  # Turkey
            'rateLimit': 1000,
            'has': {
                'cancelOrder': True,
                'CORS': True,
                'createOrder': True,
                'fetchBalance': True,
                'fetchMarkets': True,
                'fetchOHLCV': True,
                'fetchOrderBook': True,
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchTrades': True,
            },
            'timeframes': {
                '1d': '1d',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/51840849/87153926-efbef500-c2c0-11ea-9842-05b63612c4b9.jpg',
                'api': 'https://www.btcturk.com/api',
                'www': 'https://www.btcturk.com',
                'doc': 'https://github.com/BTCTrader/broker-api-docs',
            },
            'api': {
                'public': {
                    'get': [
                        'ohlcdata',  # ?last=COUNT
                        'orderbook',
                        'ticker',
                        'trades',   # ?last=COUNT(max 50)
                    ],
                },
                'private': {
                    'get': [
                        'balance',
                        'openOrders',
                        'userTransactions',  # ?offset=0&limit=25&sort=asc
                    ],
                    'post': [
                        'exchange',
                        'cancelOrder',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'maker': 0.002 * 1.18,
                    'taker': 0.003 * 1.18,
                },
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetTicker(params)
        result = []
        for i in range(0, len(response)):
            market = response[i]
            id = self.safe_string(market, 'pair')
            baseId = id[0:3]
            quoteId = id[3:6]
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            baseId = baseId.lower()
            quoteId = quoteId.lower()
            symbol = base + '/' + quote
            precision = {
                'amount': 8,
                'price': 8,
            }
            active = True
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'info': market,
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': math.pow(10, -precision['amount']),
                        'max': None,
                    },
                    'price': {
                        'min': math.pow(10, -precision['price']),
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
            })
        return result

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetBalance(params)
        result = {'info': response}
        codes = list(self.currencies.keys())
        for i in range(0, len(codes)):
            code = codes[i]
            currency = self.currencies[code]
            free = currency['id'] + '_available'
            total = currency['id'] + '_balance'
            used = currency['id'] + '_reserved'
            if free in response:
                account = self.account()
                account['free'] = self.safe_string(response, free)
                account['total'] = self.safe_string(response, total)
                account['used'] = self.safe_string(response, used)
                result[code] = account
        return self.parse_balance(result, False)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'pairSymbol': market['id'],
        }
        response = self.publicGetOrderbook(self.extend(request, params))
        timestamp = self.safe_timestamp(response, 'timestamp')
        return self.parse_order_book(response, timestamp)

    def parse_ticker(self, ticker, market=None):
        symbol = None
        if market:
            symbol = market['symbol']
        timestamp = self.safe_timestamp(ticker, 'timestamp')
        last = self.safe_number(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_number(ticker, 'high'),
            'low': self.safe_number(ticker, 'low'),
            'bid': self.safe_number(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_number(ticker, 'ask'),
            'askVolume': None,
            'vwap': None,
            'open': self.safe_number(ticker, 'open'),
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': self.safe_number(ticker, 'average'),
            'baseVolume': self.safe_number(ticker, 'volume'),
            'quoteVolume': None,
            'info': ticker,
        }

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        tickers = self.publicGetTicker(params)
        result = {}
        for i in range(0, len(tickers)):
            ticker = tickers[i]
            marketId = self.safe_string(ticker, 'pair')
            symbol = marketId
            market = None
            if marketId in self.markets_by_id:
                market = self.markets_by_id[symbol]
                symbol = market['symbol']
            result[symbol] = self.parse_ticker(ticker, market)
        return self.filter_by_array(result, 'symbol', symbols)

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        tickers = self.fetch_tickers(params)
        return self.safe_value_2(tickers, market['id'], symbol)

    def parse_trade(self, trade, market=None):
        timestamp = self.safe_timestamp(trade, 'date')
        id = self.safe_string(trade, 'tid')
        price = self.safe_number(trade, 'price')
        amount = self.safe_number(trade, 'amount')
        cost = None
        if amount is not None:
            if price is not None:
                cost = amount * price
        symbol = None
        if market is not None:
            symbol = market['symbol']
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'side': None,
            'order': None,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': None,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        # maxCount = 50
        request = {
            'pairSymbol': market['id'],
        }
        response = self.publicGetTrades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def parse_ohlcv(self, ohlcv, market=None):
        return [
            self.parse8601(self.safe_string(ohlcv, 'Time')),
            self.safe_number(ohlcv, 'Open'),
            self.safe_number(ohlcv, 'High'),
            self.safe_number(ohlcv, 'Low'),
            self.safe_number(ohlcv, 'Close'),
            self.safe_number(ohlcv, 'Volume'),
        ]

    def fetch_ohlcv(self, symbol, timeframe='1d', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {}
        if limit is not None:
            request['last'] = limit
        response = self.publicGetOhlcdata(self.extend(request, params))
        return self.parse_ohlcvs(response, market, timeframe, since, limit)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        request = {
            'PairSymbol': self.market_id(symbol),
            'OrderType': 0 if (side == 'buy') else 1,
            'OrderMethod': 1 if (type == 'market') else 0,
        }
        if type == 'market':
            if not ('Total' in params):
                raise ExchangeError(self.id + ' createOrder() requires the "Total" extra parameter for market orders(amount and price are both ignored)')
        else:
            request['Price'] = price
            request['Amount'] = amount
        response = self.privatePostExchange(self.extend(request, params))
        id = self.safe_string(response, 'id')
        return {
            'info': response,
            'id': id,
        }

    def cancel_order(self, id, symbol=None, params={}):
        request = {
            'id': id,
        }
        return self.privatePostCancelOrder(self.extend(request, params))

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        if self.id == 'btctrader':
            raise ExchangeError(self.id + ' is an abstract base API for BTCExchange, BTCTurk')
        url = self.urls['api'] + '/' + path
        if api == 'public':
            if params:
                url += '?' + self.urlencode(params)
        else:
            self.check_required_credentials()
            nonce = str(self.nonce())
            body = self.urlencode(params)
            secret = self.base64_to_binary(self.secret)
            auth = self.apiKey + nonce
            headers = {
                'X-PCK': self.apiKey,
                'X-Stamp': nonce,
                'X-Signature': self.hmac(self.encode(auth), secret, hashlib.sha256, 'base64'),
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}
