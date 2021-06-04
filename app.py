from markov import MarkovLyrics
from lyrics import scrapeLyricsText
from flask import Flask, render_template, request

app = Flask(__name__)


def generateArtistLyrics(name):
    songs = scrapeLyricsText(name)
    m = MarkovLyrics()
    for song in songs:
        m.populateMarkovChains(song)
    lyrics = m.generateLyrics()
    return lyrics.split("NEWLINE")


@app.route('/', methods=['GET', 'POST'])
def lyricsGenerator():
    lyrics = []
    if request.method == 'POST':
        artist = request.form['search']
        lyrics = generateArtistLyrics(artist)
    return render_template('home.html', lyrics=lyrics)


if __name__ == '__main__':
    app.run(debug=True)
