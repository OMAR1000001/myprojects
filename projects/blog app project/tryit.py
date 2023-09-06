import requests


all_posts= requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()[1]


print(all_posts)