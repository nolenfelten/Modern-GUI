# Modern-GUI
A buddy of mine recently got his Bachelor's Degree after publishing his thesis. When I was reviewing the paper, I saw he was using Tkinter module for the front-end of his project. 
And it bugged me! He told me his teacher never heard of Tkinter...that still bugs me!

Really, the practice using some kind of module/library to draw a window (typically by calling an OS function) for the Graphical User Interface (GUI) concept is, in my opinion, dead. Actually, no, it is not my opinion, it is deaad. Unless, of course, you are a fullscreen video game developer, in which case, this writing is not for you. 

It is all about creating a web application with your code then using your browser to execute HTML that gives you the buttons to press and input fields to type into.
Using Flask for an example:


pip install Flask


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


python app.py


Now open 127.0.0.1:5000 or localhost:5000 in your browser.




If you have to use some kind of window for your project, I propose this modern technique.
First install PyQt5:


pip install PyQt5


Then run the code in GUI.py found here in this repo.
It will create a web browser widget that you can use to execute HTML/CSS/JS.
You can even trigger JS functions from Python to send/recieve data to/from Python/JS.

Now you don't have to .pack() every freakin' thing.
.pack() my ass Tkinter!
