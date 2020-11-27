# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import RateLimitExceeded


class coinmate(Exchange):

    def describe(self):
        return self.deep_extend(super(coinmate, self).describe(), {
            'id': 'coinmate',
            'name': 'CoinMate',
            'countries': ['GB', 'CZ', 'EU'],  # UK, Czech Republic
            'rateLimit': 1000,
            'has': {
                'cancelOrder': True,
                'CORS': True,
                'createOrder': True,
                'fetchBalance': True,
                'fetchMarkets': True,
                'fetchMyTrades': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrders': True,
                'fetchTicker': True,
                'fetchTrades': True,
                'fetchTransactions': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/51840849/87460806-1c9f3f00-c616-11ea-8c46-a77018a8f3f4.jpg',
                'api': 'https://coinmate.io/api',
                'www': 'https://coinmate.io',
                'fees': 'https://coinmate.io/fees',
                'doc': [
                    'https://coinmate.docs.apiary.io',
                    'https://coinmate.io/developers',
                ],
                'referral': 'https://coinmate.io?referral=YTFkM1RsOWFObVpmY1ZjMGREQmpTRnBsWjJJNVp3PT0',
            },
            'requiredCredentials': {
                'apiKey': True,
                'secret': True,
                'uid': True,
            },
            'api': {
                'public': {
                    'get': [
                        'orderBook',
                        'ticker',
                        'transactions',
                        'tradingPairs',
                    ],
                },
                'private': {
                    'post': [
                        'balances',
                        'bitcoinCashWithdrawal',
                        'bitcoinCashDepositAddresses',
                        'bitcoinDepositAddresses',
                        'bitcoinWithdrawal',
                        'bitcoinWithdrawalFees',
                        'buyInstant',
                        'buyLimit',
                        'cancelOrder',
                        'cancelOrderWithInfo',
                        'createVoucher',
                        'dashDepositAddresses',
                        'dashWithdrawal',
                        'ethereumWithdrawal',
                        'ethereumDepositAddresses',
                        'litecoinWithdrawal',
                        'litecoinDepositAddresses',
                        'openOrders',
                        'order',
                        'orderHistory',
                        'orderById',
                        'pusherAuth',
                        'redeemVoucher',
                        'replaceByBuyLimit',
                        'replaceByBuyInstant',
                        'replaceBySellLimit',
                        'replaceBySellInstant',
                        'rippleDepositAddresses',
                        'rippleWithdrawal',
                        'sellInstant',
                        'sellLimit',
                        'transactionHistory',
                        'traderFees',
                        'tradeHistory',
                        'transfer',
                        'transferHistory',
                        'unconfirmedBitcoinDeposits',
                        'unconfirmedBitcoinCashDeposits',
                        'unconfirmedDashDeposits',
                        'unconfirmedEthereumDeposits',
                        'unconfirmedLitecoinDeposits',
                        'unconfirmedRippleDeposits',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': True,
                    'percentage': True,
                    'maker': 0.12 / 100,
                    'taker': 0.25 / 100,
                    'tiers': {
                        'taker': [
                            [0, 0.25 / 100],
                            [10000, 0.23 / 100],
                            [100000, 0.21 / 100],
                            [250000, 0.20 / 100],
                            [500000, 0.15 / 100],
                            [1000000, 0.13 / 100],
                            [3000000, 0.10 / 100],
                            [15000000, 0.05 / 100],
                        ],
                        'maker': [
                            [0, 0.12 / 100],
                            [10000, 0.11 / 100],
                            [1000000, 0.10 / 100],
                            [250000, 0.08 / 100],
                            [500000, 0.05 / 100],
                            [1000000, 0.03 / 100],
                            [3000000, 0.02 / 100],
                            [15000000, 0],
                        ],
                    },
                },
                'promotional': {
                    'trading': {
                        'maker': 0.05 / 100,
                        'taker': 0.15 / 100,
                        'tiers': {
                            'taker': [
                                [0, 0.15 / 100],
                                [10000, 0.14 / 100],
                                [100000, 0.13 / 100],
                                [250000, 0.12 / 100],
                                [500000, 0.11 / 100],
                                [1000000, 0.1 / 100],
                                [3000000, 0.08 / 100],
                                [15000000, 0.05 / 100],
                            ],
                            'maker': [
                                [0, 0.05 / 100],
                                [10000, 0.04 / 100],
                                [1000000, 0.03 / 100],
                                [250000, 0.02 / 100],
                                [500000, 0],
                                [1000000, 0],
                                [3000000, 0],
                                [15000000, 0],
                            ],
                        },
                    },
                },
            },
            'options': {
                'promotionalMarkets': ['ETH/EUR', 'ETH/CZK', 'ETH/BTC', 'XRP/EUR', 'XRP/CZK', 'XRP/BTC', 'DASH/EUR', 'DASH/CZK', 'DASH/BTC', 'BCH/EUR', 'BCH/CZK', 'BCH/BTC'],
            },
            'exceptions': {
                'exact': {
                    'No order with given ID': OrderNotFound,
                },
                'broad': {
                    'Not enough account balance available': InsufficientFunds,
                    'Incorrect order ID': InvalidOrder,
                    'Minimum Order Size ': InvalidOrder,
                    'TOO MANY REQUESTS': RateLimitExceeded,
                },
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetTradingPairs(params)
        #
        #     {
        #         "error":false,
        #         "errorMessage":null,
        #         "data": [
        #             {
        #                 "name":"BTC_EUR",
        #                 "firstCurrency":"BTC",
        #                 "secondCurrency":"EUR",
        #                 "priceDecimals":2,
        #                 "lotDecimals":8,
        #                 "minAmount":0.0002,
        #                 "tradesWebSocketChannelId":"trades-BTC_EUR",
        #                 "orderBookWebSocketChannelId":"order_book-BTC_EUR",
        #                 "tradeStatisticsWebSocketChannelId":"statistics-BTC_EUR"
        #             },
        #         ]
        #     }
        #
        data = self.safe_value(response, 'data')
        result = []
        for i in range(0, len(data)):
            market = data[i]
            id = self.safe_string(market, 'name')
            baseId = self.safe_string(market, 'firstCurrency')
            quoteId = self.safe_string(market, 'secondCurrency')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            promotionalMarkets = self.safe_value(self.options, 'promotionalMarkets', [])
            fees = self.safe_value(self.fees, 'trading')
            if self.in_array(symbol, promotionalMarkets):
                promotionalFees = self.safe_value(self.fees, 'promotional', {})
                fees = self.safe_value(promotionalFees, 'trading', fees)
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': None,
                'maker': fees['maker'],
                'taker': fees['taker'],
                'info': market,
                'precision': {
                    'price': self.safe_integer(market, 'priceDecimals'),
                    'amount': self.safe_integer(market, 'lotDecimals'),
                },
                'limits': {
                    'amount': {
                        'min': self.safe_float(market, 'minAmount'),
                        'max': None,
                    },
                    'price': {
                        'min': None,
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
        response = self.privatePostBalances(params)
        balances = self.safe_value(response, 'data')
        result = {'info': response}
        currencyIds = list(balances.keys())
        for i in range(0, len(currencyIds)):
            currencyId = currencyIds[i]
            code = self.safe_currency_code(currencyId)
            balance = self.safe_value(balances, currencyId)
            account = self.account()
            account['free'] = self.safe_float(balance, 'available')
            account['used'] = self.safe_float(balance, 'reserved')
            account['total'] = self.safe_float(balance, 'balance')
            result[code] = account
        return self.parse_balance(result)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        request = {
            'currencyPair': self.market_id(symbol),
            'groupByPriceLimit': 'False',
        }
        response = self.publicGetOrderBook(self.extend(request, params))
        orderbook = response['data']
        timestamp = self.safe_timestamp(orderbook, 'timestamp')
        return self.parse_order_book(orderbook, timestamp, 'bids', 'asks', 'price', 'amount')

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        request = {
            'currencyPair': self.market_id(symbol),
        }
        response = self.publicGetTicker(self.extend(request, params))
        ticker = self.safe_value(response, 'data')
        timestamp = self.safe_timestamp(ticker, 'timestamp')
        last = self.safe_float(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'ask'),
            'vwap': None,
            'askVolume': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_float(ticker, 'amount'),
            'quoteVolume': None,
            'info': ticker,
        }

    def fetch_transactions(self, code=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {
            'limit': 1000,
        }
        if limit is not None:
            request['limit'] = limit
        if since is not None:
            request['timestampFrom'] = since
        if code is not None:
            request['currency'] = self.currency_id(code)
        response = self.privatePostTransferHistory(self.extend(request, params))
        items = response['data']
        return self.parse_transactions(items, None, since, limit)

    def parse_transaction_status(self, status):
        statuses = {
            # any other types ?
            'COMPLETED': 'ok',
        }
        return self.safe_string(statuses, status, status)

    def parse_transaction(self, item, currency=None):
        #
        # deposits
        #
        #     {
        #         transactionId: 1862815,
        #         timestamp: 1516803982388,
        #         amountCurrency: 'LTC',
        #         amount: 1,
        #         fee: 0,
        #         walletType: 'LTC',
        #         transferType: 'DEPOSIT',
        #         transferStatus: 'COMPLETED',
        #         txid:
        #         'ccb9255dfa874e6c28f1a64179769164025329d65e5201849c2400abd6bce245',
        #         destination: 'LQrtSKA6LnhcwRrEuiborQJnjFF56xqsFn',
        #         destinationTag: null
        #     }
        #
        # withdrawals
        #
        #     {
        #         transactionId: 2140966,
        #         timestamp: 1519314282976,
        #         amountCurrency: 'EUR',
        #         amount: 8421.7228,
        #         fee: 16.8772,
        #         walletType: 'BANK_WIRE',
        #         transferType: 'WITHDRAWAL',
        #         transferStatus: 'COMPLETED',
        #         txid: null,
        #         destination: null,
        #         destinationTag: null
        #     }
        #
        timestamp = self.safe_integer(item, 'timestamp')
        amount = self.safe_float(item, 'amount')
        fee = self.safe_float(item, 'fee')
        txid = self.safe_string(item, 'txid')
        address = self.safe_string(item, 'destination')
        tag = self.safe_string(item, 'destinationTag')
        currencyId = self.safe_string(item, 'amountCurrency')
        code = self.safe_currency_code(currencyId, currency)
        type = self.safe_string_lower(item, 'transferType')
        status = self.parse_transaction_status(self.safe_string(item, 'transferStatus'))
        id = self.safe_string(item, 'transactionId')
        return {
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'currency': code,
            'amount': amount,
            'type': type,
            'txid': txid,
            'address': address,
            'tag': tag,
            'status': status,
            'fee': {
                'cost': fee,
                'currency': code,
            },
            'info': item,
        }

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        if limit is None:
            limit = 1000
        request = {
            'limit': limit,
        }
        if symbol is not None:
            market = self.market(symbol)
            request['currencyPair'] = market['id']
        if since is not None:
            request['timestampFrom'] = since
        response = self.privatePostTradeHistory(self.extend(request, params))
        items = response['data']
        return self.parse_trades(items, None, since, limit)

    def parse_trade(self, trade, market=None):
        #
        # fetchMyTrades(private)
        #
        #     {
        #         transactionId: 2671819,
        #         createdTimestamp: 1529649127605,
        #         currencyPair: 'LTC_BTC',
        #         type: 'BUY',
        #         orderType: 'LIMIT',
        #         orderId: 101810227,
        #         amount: 0.01,
        #         price: 0.01406,
        #         fee: 0,
        #         feeType: 'MAKER'
        #     }
        #
        # fetchTrades(public)
        #
        #     {
        #         "timestamp":1561598833416,
        #         "transactionId":"4156303",
        #         "price":10950.41,
        #         "amount":0.004,
        #         "currencyPair":"BTC_EUR",
        #         "tradeType":"BUY"
        #     }
        #
        marketId = self.safe_string(trade, 'currencyPair')
        market = self.safe_market(marketId, market, '_')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'amount')
        cost = None
        if amount is not None:
            if price is not None:
                cost = price * amount
        side = self.safe_string_lower_2(trade, 'type', 'tradeType')
        type = self.safe_string_lower(trade, 'orderType')
        orderId = self.safe_string(trade, 'orderId')
        id = self.safe_string(trade, 'transactionId')
        timestamp = self.safe_integer_2(trade, 'timestamp', 'createdTimestamp')
        fee = None
        feeCost = self.safe_float(trade, 'fee')
        if feeCost is not None:
            fee = {
                'cost': feeCost,
                'currency': market['quote'],
            }
        takerOrMaker = self.safe_string(trade, 'feeType')
        takerOrMaker = 'maker' if (takerOrMaker == 'MAKER') else 'taker'
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'type': type,
            'side': side,
            'order': orderId,
            'takerOrMaker': takerOrMaker,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'currencyPair': market['id'],
            'minutesIntoHistory': 10,
        }
        response = self.publicGetTransactions(self.extend(request, params))
        #
        #     {
        #         "error":false,
        #         "errorMessage":null,
        #         "data":[
        #             {
        #                 "timestamp":1561598833416,
        #                 "transactionId":"4156303",
        #                 "price":10950.41,
        #                 "amount":0.004,
        #                 "currencyPair":"BTC_EUR",
        #                 "tradeType":"BUY"
        #             }
        #         ]
        #     }
        #
        data = self.safe_value(response, 'data', [])
        return self.parse_trades(data, market, since, limit)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        response = self.privatePostOpenOrders(self.extend({}, params))
        extension = {'status': 'open'}
        return self.parse_orders(response['data'], None, since, limit, extension)

    def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOrders requires a symbol argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'currencyPair': market['id'],
        }
        # offset param that appears in other parts of the API doesn't appear to be supported here
        if limit is not None:
            request['limit'] = limit
        response = self.privatePostOrderHistory(self.extend(request, params))
        return self.parse_orders(response['data'], market, since, limit)

    def parse_order_status(self, status):
        statuses = {
            'FILLED': 'closed',
            'CANCELLED': 'canceled',
            'PARTIALLY_FILLED': 'open',
            'OPEN': 'open',
        }
        return self.safe_string(statuses, status, status)

    def parse_order_type(self, type):
        types = {
            'LIMIT': 'limit',
            'MARKET': 'market',
        }
        return self.safe_string(types, type, type)

    def parse_order(self, order, market=None):
        #
        # limit sell
        #
        #     {
        #         id: 781246605,
        #         timestamp: 1584480015133,
        #         trailingUpdatedTimestamp: null,
        #         type: 'SELL',
        #         currencyPair: 'ETH_BTC',
        #         price: 0.0345,
        #         amount: 0.01,
        #         stopPrice: null,
        #         originalStopPrice: null,
        #         marketPriceAtLastUpdate: null,
        #         marketPriceAtOrderCreation: null,
        #         orderTradeType: 'LIMIT',
        #         hidden: False,
        #         trailing: False,
        #         clientOrderId: null
        #     }
        #
        # limit buy
        #
        #     {
        #         id: 67527001,
        #         timestamp: 1517931722613,
        #         trailingUpdatedTimestamp: null,
        #         type: 'BUY',
        #         price: 5897.24,
        #         remainingAmount: 0.002367,
        #         originalAmount: 0.1,
        #         stopPrice: null,
        #         originalStopPrice: null,
        #         marketPriceAtLastUpdate: null,
        #         marketPriceAtOrderCreation: null,
        #         status: 'CANCELLED',
        #         orderTradeType: 'LIMIT',
        #         hidden: False,
        #         avgPrice: null,
        #         trailing: False,
        #     }
        #
        id = self.safe_string(order, 'id')
        timestamp = self.safe_integer(order, 'timestamp')
        side = self.safe_string_lower(order, 'type')
        price = self.safe_float(order, 'price')
        amount = self.safe_float(order, 'originalAmount')
        remaining = self.safe_float(order, 'remainingAmount')
        if remaining is None:
            remaining = self.safe_float(order, 'amount')
        status = self.parse_order_status(self.safe_string(order, 'status'))
        type = self.parse_order_type(self.safe_string(order, 'orderTradeType'))
        filled = None
        cost = None
        if (amount is not None) and (remaining is not None):
            filled = max(amount - remaining, 0)
            if remaining == 0:
                status = 'closed'
            if price is not None:
                cost = filled * price
        average = self.safe_float(order, 'avgPrice')
        marketId = self.safe_string(order, 'currencyPair')
        symbol = self.safe_symbol(marketId, market, '_')
        clientOrderId = self.safe_string(order, 'clientOrderId')
        stopPrice = self.safe_float(order, 'stopPrice')
        return {
            'id': id,
            'clientOrderId': clientOrderId,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': type,
            'timeInForce': None,
            'side': side,
            'price': price,
            'stopPrice': stopPrice,
            'amount': amount,
            'cost': cost,
            'average': average,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'trades': None,
            'info': order,
            'fee': None,
        }

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        method = 'privatePost' + self.capitalize(side)
        request = {
            'currencyPair': self.market_id(symbol),
        }
        if type == 'market':
            if side == 'buy':
                request['total'] = self.amount_to_precision(symbol, amount)  # amount in fiat
            else:
                request['amount'] = self.amount_to_precision(symbol, amount)  # amount in fiat
            method += 'Instant'
        else:
            request['amount'] = self.amount_to_precision(symbol, amount)  # amount in crypto
            request['price'] = self.price_to_precision(symbol, price)
            method += self.capitalize(type)
        response = getattr(self, method)(self.extend(request, params))
        id = self.safe_string(response, 'data')
        return {
            'info': response,
            'id': id,
        }

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderId': id,
        }
        market = None
        if symbol:
            market = self.market(symbol)
        response = self.privatePostOrderById(self.extend(request, params))
        data = self.safe_value(response, 'data')
        return self.parse_order(data, market)

    def cancel_order(self, id, symbol=None, params={}):
        #   {"error":false,"errorMessage":null,"data":{"success":true,"remainingAmount":0.01}}
        request = {'orderId': id}
        response = self.privatePostCancelOrderWithInfo(self.extend(request, params))
        return {
            'info': response,
        }

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'] + '/' + path
        if api == 'public':
            if params:
                url += '?' + self.urlencode(params)
        else:
            self.check_required_credentials()
            nonce = str(self.nonce())
            auth = nonce + self.uid + self.apiKey
            signature = self.hmac(self.encode(auth), self.encode(self.secret))
            body = self.urlencode(self.extend({
                'clientId': self.uid,
                'nonce': nonce,
                'publicKey': self.apiKey,
                'signature': signature.upper(),
            }, params))
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is not None:
            if 'error' in response:
                # {"error":true,"errorMessage":"Minimum Order Size 0.01 ETH","data":null}
                if response['error']:
                    message = self.safe_string(response, 'errorMessage')
                    feedback = self.id + ' ' + message
                    self.throw_exactly_matched_exception(self.exceptions['exact'], message, feedback)
                    self.throw_broadly_matched_exception(self.exceptions['broad'], message, feedback)
                    raise ExchangeError(self.id + ' ' + self.json(response))
        if code > 400:
            if body:
                feedback = self.id + ' ' + body
                self.throw_exactly_matched_exception(self.exceptions['exact'], body, feedback)
                self.throw_broadly_matched_exception(self.exceptions['broad'], body, feedback)
                raise ExchangeError(feedback)  # unknown message
            raise ExchangeError(self.id + ' ' + body)
