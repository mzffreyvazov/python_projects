import telebot
import subprocess
# Set up your bot
bot = telebot.TeleBot('6304860990:AAGwZ6vuYhsXfIbecTk7rVPmtnOeEZDdRAs')

@bot.message_handler(commands=['export'])
def request_playlist_link(message):
    # Send a message requesting the playlist link
    bot.reply_to(message, "Please provide the YouTube playlist link.")

    # Register the next handler to receive the playlist link
    bot.register_next_step_handler(message, download_playlist)

def download_playlist(message):
    # Extract the playlist link from the message text
    playlist_link = message.text

    try:
        # Execute the youtube-dl command to download the playlist
        subprocess.call(['youtube-dl', '-i', '--extract-audio', '--audio-format', 'mp3', '--yes-playlist', playlist_link])

        # Send the downloaded music files to the user
        send_music_files(message.chat.id)

        bot.reply_to(message, "Playlist downloaded successfully.")
    except Exception as e:
        error_message = "An error occurred while downloading the playlist. Please try again later."
        print(e)
        bot.reply_to(message, error_message)

def send_music_files(chat_id):
    # Get the list of downloaded music files
    music_files = subprocess.check_output(['ls', '-1', '*.mp3']).decode().split('\n')
    music_files = [file for file in music_files if file]  # Remove empty entries

    # Send each music file to the user
    for file in music_files:
        with open(file, 'rb') as audio:
            bot.send_audio(chat_id, audio)

# Start the bot
bot.polling()


