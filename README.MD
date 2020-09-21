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
- Clone or Download this repository ⏬
- Open the Terminal 🐱‍💻
- Move inside 👉 the your cloned copy of the repo 

```cd GitKundli```
- Now make sure you have all the dependencies🧱 

```pip install -r requirements.txt```

- Visit this [link](https://github.com/settings/tokens) and Click on ```Generate new token```
- Intially select all the options. [ Note: Later on you can come back, delete this token and generate a new one with only the permissions you think are necessary]
- Don't forget to give a name to the token ( say ```gitkundli``` )
- Copy the alphanumeric value of the taken [and save it in a text file for future reference. Remember you can only access this once on GitHub]
- Now add an environment variable to your system such that name is ```GITHUB_TOKEN``` and value is the one you copied earlier. 
- Return back inside your cloned repo ```GitKundli```
- Now let's run our script and store our results in a csv file ```python gitkundli.py```

<h2 align = 'center'>License 📜</h2>
<p align = 'center'><img src = 'https://media.giphy.com/media/XfD8VJDUurgMjNEP72/giphy.gif' width = 40%></p>

[MIT License](./LICENSE)
