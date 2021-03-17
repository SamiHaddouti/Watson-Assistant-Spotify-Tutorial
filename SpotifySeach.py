#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#

#importing necessary libraries 
import sys
import subprocess
import json

#function to install packages to import a library in code
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#install the library Spotify to work with the Spotify API
install("spotipy")

#importing Spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#save your credentials as variables
client_id = '2de12ab8c69d499da5e164025b612f7f'
client_secret = '069fcfb73da04c31920a197265703829'

#acessing the spotify web api through our credentials
credentials = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=credentials)

#creating a function to search an artist within the Spotify API
#argument "artist" is the input and should contain the name of the artist
def search_artist(artist):
    search = spotify.search(q=artist, limit=1, offset=0, type='artist', market=None) 
    #q stands for the query looking for the artist argument; limit limits the amount of results; offset=0 sets the index of the first result to 0; type defines what we are looking for; market defines the market we are looking into
    items_found = len(search["artists"]["items"])

    if items_found == 0:
        error = "Error. Spotify could not find the track."
        return error
    else:
        for i in range(items_found): #the loop is only necessary if you want to increase the amount of results (limit > 1 )
            result = search["artists"]["items"][i]["external_urls"]["spotify"]
            #to find the url to the item (album) we are looking for we need to acces a certain array element in the multi-dimensional array structure
    return result

#function to search an album
def search_album(album):
    search = spotify.search(q=album, limit=1, offset=0, type='album', market=None)
    items_found = len(search["albums"]["items"])
    
    if items_found == 0:
        error = "Error. Spotify could not find the track."
        return error
        #if the search finds no items the function should return an error message
    else:
        for i in range(items_found):
            result = search["albums"]["items"][i]["external_urls"]["spotify"]
    return result
    
#function to search a track    
def search_track(track=""):
    search = spotify.search(q=track, limit=1, offset=0, type='track', market=None)
    items_found = len(search["tracks"]["items"])

    if  items_found == 0:
        error = "Error. Spotify could not find the track."
        return error
    else:
        for i in range(items_found):
            result = search["tracks"]["items"][i]["external_urls"]["spotify"]
    return result

#main function to acces the function depending on the input (dict)
def main(dict):
    
    search = dict["search"]
    item = dict["item"]
    #saving the input parameters for the search (f.e. "search_track") as search and the item we are looking for (f.e. "Smells Like Teen Spirit") as item
    
    if search == "search_artist":
        end_result = json.dumps(search_artist(item))
        return { "message": end_result }
    elif search == "search_album":
        end_result = json.dumps(search_album(item))
        return { "message": end_result }
    elif search == "search_track":
        end_result = json.dumps(search_track(item))
        return { "message": end_result }
        
    #with that if-construct the type of search input is being compared to the three functions and matched to the one required for the sepcific search
    #then we pass on the input parameter "item" to receive a result
    #the result then needs to be returned in JSON-format 
   
    
    