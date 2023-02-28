# Первый вопрос

# Если говорить о зависимости ETH от BTC, то четкой корреляции нет. Мнение о том, что биткоин влияет на все
# криптовалюты, появилось из-за общей тенденции роста цен в 2017 г. и падения в 2018 году. Однако в целом активность
# по рынку криптовалют снижается, капитализация также не отличается активным ростом, поэтому любые всплески покупок
# Ethereum пока что можно назвать лишь дыханием рынка, которому свойственно расти или снижаться — порой без четко
# выраженной тенденции

# Если честно, первое задание я не совсем понял, но сделал его в своем понимании.

# Второй вопрос
# pip install pybit

from pybit import spot
import time

session = spot.HTTP(endpoint="https://api.bybit.com")
symbol = session.orderbook(symbol="ETHUSDT")
old_price = float(symbol['result']['asks'][0][0])

for _ in range(3600):
    session = spot.HTTP(endpoint="https://api.bybit.com")
    symbol = session.orderbook(symbol="ETHUSDT")
    new_price = float(symbol['result']['asks'][0][0])
    if new_price > (old_price + (old_price * 0.01)) or new_price < (old_price - (old_price * 0.01)):
        old_price = new_price
        print(new_price)
    time.sleep(1)