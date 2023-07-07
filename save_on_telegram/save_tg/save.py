import telebot
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

# create a bot object with your bot token
bot = telebot.TeleBot('your_token')
spotify_client = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials(client_id='your_client_id', client_secret='your_client_secret'))

# define a function to handle incoming messages
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Hello, welcome to my bot!')


user_states = {}

@bot.message_handler(commands=['export'])
def export_playlist(message):
    chat_id = message.chat.id

    # Set the user state to expect the playlist link
    user_states[chat_id] = 'waiting_for_link'
    
    bot.send_message(chat_id=chat_id, text="Please provide the link to the playlist.")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_for_link')
def process_playlist_link(message):
    chat_id = message.chat.id
    playlist_link = message.text

    # Reset the user state
    user_states.pop(chat_id)
    playlist_id = playlist_link.split('/')[-1].split('?')[0]

    # Fetch playlist details from Spotify API
    playlist = spotify_client.playlist(playlist_id)

    # Extract relevant information from the playlist response
    playlist_name = playlist['name']
    playlist_owner = playlist['owner']['display_name']
    playlist_tracks = playlist['tracks']['total']

    # Generate the export message with playlist details
    export_message = f"Playlist: {playlist_name}\nOwner: {playlist_owner}\nTracks: {playlist_tracks}"
    i = 0
    while i<5:
        for track in playlist['tracks']['items']:
                # Get the track details
                track_name = track['track']['name']
                track_artist = track['track']['artists'][0]['name']
                track_preview_url = track['track']['preview_url']

                # Download the track file
                response = requests.get(track_preview_url)
                if response.status_code == 200:
                    # Save the track file locally
                    with open(f'{track_name}.mp3', 'wb') as file:
                        file.write(response.content)

                    # Send the track as an audio message
                    with open(f'{track_name}.mp3', 'rb') as audio:
                        bot.send_audio(chat_id=message.chat.id, audio=audio, caption=f'{track_name} - {track_artist}')
        i += 1
 
    # Send the export message as a reply
    bot.reply_to(message, export_message)

    bot.send_message(chat_id=chat_id, text="Playlist link received and processed.")


# start the bot
bot.polling()

