from flask import Flask, render_template

app = Flask(__name__)

# Your projects data here
projects = [
    {
        "name": "Personal Portfolio",
        "description": "Portfolio built with Flask.",
        "tech": "Flask, HTML, CSS",
        "link": "https://github.com/juhi/portfolio"
    },
    {
        "name": "Civil Engineer Website",
        "description": "A civil engineer having a business for the same, i made website including all details",
        "tech": "Python, Tkinter",
        "link": "https://bpn-port-smih.vercel.app/about"
    },
    {
        "name": "Gate Exam Series",
        "description": "Specifically designed for CSE and DA branch though to practice each subject with levels of difficulty according to needs",
        "tech": "Python, Flask, API",
        "link": "https://gate-rho.vercel.app/"
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

