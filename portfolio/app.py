from flask import Flask, render_template

app = Flask(__name__)

# Your projects data here
projects = [
    {
        "name": "Personal Portfolio",
        "description": "Portfolio built with Flask.",
        "tech": "Flask, HTML, CSS",
        "link": "https://github.com/juhi/portfolio"
    }
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route('/contact')
def contact():
    return render_template("contact.html")

# This line ensures Vercel can run the Flask app
if __name__ == "__main__":
    app.run()
