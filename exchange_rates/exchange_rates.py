import currencylayer

# https://currencylayer.com/
""" http://rates.fxcm.com/RatesXML """

id = '70328459c4f025e2caa21f63447db598'
#id = ' '

rates_reader = currencylayer.Client(id)

usd_rates = rates_reader.live_rates(base_currency='USD')

if usd_rates['success'] == True:

    try:
        usd_quotes = usd_rates['quotes']
    except KeyError as err:
        print('Invalid key {}'.format(err))
    else:
        for pair, rate in usd_quotes.items():
            print(pair, pair[3:], rate)
    finally:
        print('\b' 'DONE!')

else:
    print('ERROR {}'.format(usd_rates))



