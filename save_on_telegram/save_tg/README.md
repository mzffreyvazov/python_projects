# Telegram Bot for Exporting Spotify Playlist

This is a Python script that implements a Telegram bot for exporting Spotify playlists. Telegram is a great place for exporting your Spotify playlist and 
listening the musics easily with no internet connection needed after exporting. You can also easily save the musics to you device's internal storage, so it is also a great way to
download you spotify playlist to your device.
The bot allows users to provide a Spotify playlist link and then downloads and sends audio messages for each track in the playlist. 
Biggest downside is this: Spotify doesn't allow downloading the full tracks, but only their 30-second previews (and I was not aware of this fack until I finally finished writing this python script.)

## Prerequisites

To run this script, you need to have the following:

- Python 3.x installed on your system
- The following Python libraries:
  - `telebot`: To interact with the Telegram Bot API
  - `spotipy`: To interact with the Spotify API
  - `requests`: To make HTTP requests

You also need to have a Spotify account and a Telegram bot token. Additionally, you should obtain a Spotify client ID and client secret by creating a Spotify application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

## Installation

1. Clone the repository and navigate to the project directory:

   ```shell
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
2. Install the required Python libraries using `pip`:
   ```bash
   pip install telebot spotipy requests
3. Open the Python script in a text editor and replace the following placeholders with your own credentials:
   - `your_token`: Replace with your Telegram bot token
   - `your_client_id`: Replace with your Spotify client ID
   - `your_client_secret`: Replace with your Spotify client secret
  
## Usage

1. Run the Python script:
   ```bash
   python bot.py
2. Start a conversation with your Telegram bot.
3. Send the `/start` command to receive a welcome message.
4. To export a playlist, send the `/export` command.
5. Provide the link to the Spotify playlist when prompted by the bot.
6. The bot will download each track from the playlist and send it as an audio message. It will also display details about the playlist, including the name, owner, and number of tracks.
7. Note: The bot will only download and send the first 5 tracks of the playlist for demonstration purposes. You can modify the code to handle all tracks or a specific number of tracks based on your requirements.
8. Once the export is complete, the bot will send a message indicating that the playlist link has been received and processed.

