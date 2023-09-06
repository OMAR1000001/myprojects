import requests
import datetime


shee_dat=requests.get(url="https://api.sheety.co/2a4a03406c27832b99f31d7ed2680d6f/flightDealsCopy/prices")
pices=shee_dat.json()['prices']
city=[city['city'] for city in pices]
iata_city=[city['iataCode'] for city in pices]

flihgt_tquila="W5OAXZmiHDv8cQ3tXth1TsEubV3UTqf0"

from_today=datetime.datetime.now().strftime("%d/%m/%Y")
to_thatday=(datetime.datetime.today()+datetime.timedelta(days=15)).strftime("%d/%m/%Y")

prices=1000
lista={}

for capitals in iata_city :
    Parameters = {
        "search_id": "3c92b5e6-0e59-ac79-3879-823a015778bd",
        "fly_from": "CAI",
        "fly_to": capitals,
        "date_from": from_today,
        "date_to": to_thatday,

    }
    headers = {
        "apikey": flihgt_tquila,
    }

    flihgts = requests.get(url="https://api.tequila.kiwi.com/v2/search?", params=Parameters, headers=headers)

    data = flihgts.json()['data']
    capital_mon = [capt['price'] for capt in data]

    if capital_mon != []:
        min_capital=min(capital_mon)
        citys = [cit['city'] for cit in pices]
        for citu in citys:
            price={
                "City":f"{citu}",
                "IATA Code":capitals,
                "Lowest Price":min_capital,

            }

            send=requests.post("https://api.sheety.co/2a4a03406c27832b99f31d7ed2680d6f/flightDealsCopy/prices",json=price)
            lista.append(price)







print(lista)


