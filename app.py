from flask import Flask, render_template, request
import wikipediaapi

app = Flask(__name__)

# Initialize the Wikipedia API with a custom User-Agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en'
)
wiki_wiki._session.headers.update({
    "User-Agent": "MyWikiApp/1.0 (https://github.com/shashwatkanungo/Flask_Wikipedia-Information-Retrival)"
})

@app.route('/')
def home():
    return render_template('index.html')   # homepage with a search form

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'] 
    page = wiki_wiki.page(query)  # fetch Wikipedia page

    if page.exists():
        title = page.title
        summary = page.summary[0:500]  # fetch the first 500 characters
        url = page.fullurl
        return render_template('result.html', title=title, summary=summary, url=url)
    else:
        return render_template('result.html', error="No article found")

if __name__ == '__main__':
    app.run(debug=True)
