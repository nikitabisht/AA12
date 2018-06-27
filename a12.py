#question1

print("Access tokens are the thing that applications use to make API requests on behalf of a user. The access token represents the authorization of a specific application to access specific parts of a user’s data.")
from n11 import C,A,Access,AccessToken
print(AccessToken)

#end

#question2

import socket

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')
addr3 = socket.gethostbyname('facebook.com')

print(addr1)
print(addr2)
print(addr3)

#end

#question3

from n11 import C,A,Access,AccessToken
import tweepy
oauth=tweepy.OAuthHandler(C,A)
oauth.set_access_token(AccessToken,Access)
api=tweepy.API(oauth)
user=api.search('#veere di wedding')

#end

#question4

print("A Library is a chunk of code that you can call from your own code, to help you do things more quickly/easily. For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you having to write all that code for yourself. Typically a library will only offer one area of functionality (processing images or operating on zip files")

print("An API (application programming interface) is a term meaning the functions/methods in a library that you can call to ask it to do things for you - the interface to the library.")

#end

#question5

from n11 import C,A,Access,AccessToken
import  tweepy

oauth=tweepy.OAuthHandler(C,A)
oauth.set_access_token(AccessToken,Access)
api= tweepy.API(oauth)
print(api.search("#sanju"))

user=api.get_user('nikita_bisht05')
print(user.screen_name)
print(user.followers_count)

#end

