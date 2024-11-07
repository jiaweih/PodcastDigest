from flask import Flask, render_template, request
from quickpod import summarize, download_spotify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_url():
    podcast_url = request.form['url']
    audio_path = download_spotify(podcast_url)
    field_id = 101
    transcript, summary = summarize(audio_path, field_id)
    return render_template('index.html', transcript=transcript, summary=summary)

if __name__ == 'main':
    app.run(debug=True)


# from flask import Flask, render_template, request, session
# from quickpod import summarize
# import requests

# # app = Flask(__name__)

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     search_results = session.get('search_results', [])
# #     session['search_results'] = []
# #     return render_template('index.html', search_results=search_results)

# # @app.route('/submit', methods=['POST'])
# # def submit():
# #     podcast_url = request.form['url']
# #     # search_results = []
# #     # Call an external API to search for the HTML value in the search results
# #     # response = requests.get(f'https://api.example.com/search?q={podcast_url}')
# #     audio_path = download_spotify(podcast_url)
# #     transcript = summarize(audio_path, file_id)
# #     # if response.status_code == 200:
# #     # search_results = response.json()
# #     session['search_results'] = transcript
# #     return redirect(url_for('index'))

# # if __name__ == 'main':
# #     app.run(debug=True)

# from flask import Flask, render_template, request
# from quickpod import summarize

# # name = "quickpod"

# app = Flask(__name__)
# transcript = "show this"

# @app.route('/submit', methods=['POST'])
# def submit():
#     podcast_url = request.form['url']
#     search_results = []
#     print(podcast_url)
#     file_id = 101
#     # Do something with the HTML value
#     # podcast_url = "https://open.spotify.com/episode/6edTClXMUOX5BEMgseBMSr?si=7U5OdqeIQFS4S_zmNuNYww"
#     audio_path = download_spotify(podcast_url)
#     transcript = summarize(audio_path, file_id)
#     session['search_results'] = transcript
#     # return 'Success!'
#     return render_template('index.html', summary='foo')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     url = transcript
#     summary = 'summary'
#     # if request.method == 'POST':
#         # url = request.form['url']
#         # Add your code to generate a summary from the URL here
#         # search_results = session.get('search_results', [])
#         # session['search_results'] = []
#     search_results = request.args.get('search_results', [])
#     summary = f"Summary for {search_results}"
#     # return render_template('index.html', search_results=search_results, url=url)
#     return render_template('new_page.html', search_results=search_results)
#     # return render_template('index.html', search_results=search_results, url=url, summary=summary)
#     # return render_template('index.html', url=url, summary=summary)


# # def index():
# #     search_results = session.get('search_results', [])
# #     session['search_results'] = []
# #     return render_template('index.html', search_results=search_results)

# if __name__ == 'main':
#     app.run(debug=True)


# # # @app.route('/submit', methods=['POST'])
# # # def submit():
# # #     html_value = request.form['html_field_name']
# # #     search_results = []
# # #     # Call an external API to search for the HTML value in the search results
# # #     response = requests.get(f'https://api.example.com/search?q={html_value}')
# # #     if response.status_code == 200:
# # #         search_results = response.json()
# # #     session['search_results'] = search_results
# #     # return redirect(url_for('index'))


# # from flask import Flask, render_template, request, redirect, url_for, session

# # app = Flask(__name__)
# # # app.secret_key = 'someSecretKey'

# # # Placeholder functions for your existing logic
# # def download_spotify(url):
# #     return "path/to/audio"

# # def summarize(audio_path, file_id):
# #     return "Summary of the podcast"

# # @app.route('/', methods=['GET'])
# # def index():
# #     summary = session.get('search_results', None)
# #     return render_template('index.html', summary=summary)

# # @app.route('/submit', methods=['POST'])
# # def submit():
# #     podcast_url = request.form['url']
# #     print(podcast_url)
# #     file_id = 101
# #     audio_path = download_spotify(podcast_url)
# #     transcript = summarize(audio_path, file_id)
# #     session['search_results'] = transcript
# #     return redirect(url_for('index'))

# # if __name__ == '__main__':
# #     app.run(debug=True)
