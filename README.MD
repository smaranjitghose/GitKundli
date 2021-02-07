<h1 align = "center">Git Kundli📑</h1>

At times we need to fetch some data📈 from our GitHub like details about the pull requests🩹 to some of our repositories in an open source🤝 program.

<p align = "center"><img src = "https://media.giphy.com/media/3osxYc2axjCJNsCXyE/giphy.gif"></p>

Larger the data, the more cumbersome😪 it becomes to fetch, analyze and derive the desired inference

<p align = "center"><img src = "https://media.giphy.com/media/l2JhpjWPccQhsAMfu/giphy.gif"></p>

What if we could automate🤖 it?

<p align = "center"><img src = "<p align = "center"><img src = "https://media.giphy.com/media/fwfbJvRNHb5sI/giphy.gif" width = 40%></p>

Well, using a simple python🐍 script with a GraphQL⚛ query can save the day for us!

## How to use this?

<p align = "center"><img src = "https://media.giphy.com/media/26AHPxxnSw1L9T1rW/giphy.gif" width = 60%></p>

- I assume you have Anaconda installed in your operating system and set to path. If not, please visit this [link](https://docs.anaconda.com/anaconda/install/) and do it

- Clone or download this repository ⏬

- Open the Terminal 🐱‍💻

- Move inside 👉 the your cloned copy of the repo

`cd GitKundli`

- Now make sure you have all the dependencies🧱

`pip install -r requirements.txt`

- Time to run our app

`streamlit run app.py`

- Open `http://localhost:8502` or the link displayed in the terminal where the streamlit app is running on your local server

- Visit this [link](https://github.com/settings/tokens) and Click on `Generate new token`

- Initially select all the options. [ Note: Later on you can come back, delete this token and generate a new one with only the permissions you think are necessary]

- Don't forget to give a name to the token ( say `gitkundli` )

- Copy the alphanumeric value of the taken [and save it in a text file for future reference. Remember you can only access this once on GitHub]
- Return back your hosted app

- Open Specific Pages, Give the Token, Some related Information, Make use of the output!

- Now let's run our script and store our results in a csv file `python gitkundli.py`

## License 📜

<p align = 'center'><img src = 'https://media.giphy.com/media/XfD8VJDUurgMjNEP72/giphy.gif' width = 40%></p>

[MIT License](./LICENSE)
