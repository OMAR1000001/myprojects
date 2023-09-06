# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
#     pass

import requests
import datetime


shee_dat=requests.get(url="https://api.sheety.co/2a4a03406c27832b99f31d7ed2680d6f/flightDealsCopy/prices")
pices=shee_dat.json()
print(pices)
# citys = [cit['city'] for cit in pices]
# print(citys)
# city=[city['city'] for city in pices]
# iata_city=[city['iataCode'] for city in pices]
#
# for citu in citys:
#     print(citu)
# print(iata_city)
#
# flihgt_tquila="W5OAXZmiHDv8cQ3tXth1TsEubV3UTqf0"
#
# from_today=datetime.datetime.now().strftime("%d/%m/%Y")
# to_thatday=(datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%d/%m/%Y")
#
# prices=1000
# lista=[]
#
# for capitals in iata_city :
#     Parameters = {
#         "search_id": "3c92b5e6-0e59-ac79-3879-823a015778bd",
#         "fly_from": capitals,
#         "fly_to": "FRA",
#         "date_from": from_today,
#         "date_to": to_thatday,
#
#     }
#     headers = {
#         "apikey": flihgt_tquila,
#     }
#
#     flihgts = requests.get(url="https://api.tequila.kiwi.com/v2/search?", params=Parameters, headers=headers)
#
#     data = flihgts.json()['data']
    # prices = int(pric['price'])
    # import requests
    # # import requests
    #
    # c=[cit for cit in data]
    # print(c)
    # capital =[capt['price'] for capt in data]
    #
    # if capital != []:
    #     print(min(capital))

        # import requests
        # import datetime
        #
        # shee_dat = requests.get(url="https://api.sheety.co/2a4a03406c27832b99f31d7ed2680d6f/flightDealsCopy/prices")
        # pices = shee_dat.json()['prices']
        # city = [city['city'] for city in pices]
        # iata_city = [city['iataCode'] for city in pices]
        #
        # flihgt_tquila = "W5OAXZmiHDv8cQ3tXth1TsEubV3UTqf0"
        #
        # from_today = datetime.datetime.now().strftime("%d/%m/%Y")
        # to_thatday = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        #
        # prices = 1000
        # lista = []
        #
        # for capitals in iata_city:
        #     Parameters = {
        #         "search_id": "3c92b5e6-0e59-ac79-3879-823a015778bd",
        #         "fly_from": capitals,
        #         "fly_to": "FRA",
        #         "date_from": from_today,
        #         "date_to": to_thatday,
        #
        #     }
        #     headers = {
        #         "apikey": flihgt_tquila,
        #     }
        #
        #     flihgts = requests.get(url="https://api.tequila.kiwi.com/v2/search?", params=Parameters, headers=headers)
        #
        #     data = flihgts.json()['data']
        #
        #     name = ""
        #     for pric in data:
        #         if capitals == name:
        #             if int(pric['price']) < prices:
        #                 prices = int(pric['price'])
        #                 copy = {
        #                     capitals: pric['price'],
        #                 }
        #                 lista.append(copy)
        #
        #         else:
        #             capitals = name
        #             prices = int(pric['price'])
        #             copy = {
        #                 capitals: pric['price'],
        #             }
        #             lista.append(copy)
        #
        # print(lista)