# -*- coding: utf-8 -*-

import oauth2 as oauth
import json
import time
import pymongo

CONSUMER_KEY = "Ur5J5gHT6uYg7zms7GaLUNYWf"
CONSUMER_SECRET = "SXSyveGpYiTzjifwC84IZ7IJBP7Lx138nODPhGW7CkykjIKTyu"
ACCESS_KEY = "2471507719-kvni00S7JySj8Iq3PUD80d01jrh8HpSodLnoABo"
ACCESS_SECRET = "EjbRRnAf9E8CgedjX9qBZ2XZABnRGI8vHeHft50CU6f8S"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

clientMongo = pymongo.MongoClient("localhost", 27017)
db = clientMongo.db_cores_observatory

#since_id = '' #pode usar since_id ou nao, se usar, colocar na url

#Geolocalização da Central do Brasil
#Latitude, Longitude, Raio Radius ao redor da posição.
#Com este radius de 70km, a área abrange toda Região Metropolitana do RJ.
#geo='-22.903426,-43.191478,70km'

#Desde. Formato YYYY-MM-DD.
since='2018-04-17'

#Até o dia anterior de. Formato YYYY-MM-DD.
until='2018-04-24'

#Lista de Termos, separe por vírgulas.

query = ['vereadora','marielle','mariellefranco','mariellevive','naofoiassalto','mariellepresente','mariellefrancopresente','todospormarielle','justicaparamarielle','pormarielleeanderson']

for q in query:

        max_id = '0'
        contadorTweets = 0
        continua = 1

        while(continua == 1):
                try:

                        if(max_id == '0'):

                                URL = "https://api.twitter.com/1.1/search/tweets.json?q="+q+"&since="+since+"&until="+until+"&count=100"
                        else:

                                URL = "https://api.twitter.com/1.1/search/tweets.json?q="+q+"&since="+since+"&until="+until+"&count=100"+"&max_id="+str(max_id)
                        max_id_ant = max_id
                        response, data = client.request(URL, "GET")
                        vereadoraMarielleFranco20180417 = json.loads(data)
                        for tweet in vereadoraMarielleFranco20180417['statuses']:
                                                        
                                db.vereadoraMarielleFranco20180417.update({'id': tweet['id']},tweet, upsert=True)
                                contadorTweets = contadorTweets + 1
                                tweet['text']==dict
                                tx = tweet['text']
                                print "Termo Buscado: "+ q
                                print "\n"
                                print str("Tweet: " + tx.encode('utf-8'))
                                print "\n"
                                print "Número de tweets com termo atual: "
                                print contadorTweets
                                print "\n"
                                print "ID do Tweet: "
                                print max_id
                                print '======================================================'
                                max_id = tweet['id'] - 1
                                
                        time.sleep(2)
                        if(max_id == max_id_ant):                                
                                continua = 0
                        
                except Exception, e:

                        print e
                        print 'dormiu'
                        time.sleep(15*60)
                        pass
