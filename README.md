<p align="center">
</p>

<h2 align="center">Intelligent Text Parsing - ONDC</h2>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platform](https://img.shields.io/badge/platform-reddit-orange.svg)](https://www.reddit.com/user/Wordbook_Bot)
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

A solution to intelligent text parsing for the ONDC innovation hackathon.

## 💭 How it works <a name = "working"></a>

The bot first extracts the word from the comment and then fetches word definitions, part of speech, example and source from the Oxford Dictionary API.

If the word does not exist in the Oxford Dictionary, the Oxford API then returns a 404 response upon which the bot then tries to fetch results form the Urban Dictionary API.

The bot uses the Pushshift API to fetch comments, PRAW module to reply to comments and Heroku as a server.

The entire bot is written in Python 3.6

## 🎈 Usage <a name = "usage"></a>

## 🏁 Getting Started <a name = "getting_started"></a>

Set up the packages

1. for python:
   1. install pipenv ( `pip install pipenv`)
   2. install packages using pipenv (`pipenv install`)
   3. run the app using main.py (`pipenv run python main.py`)
2. for react frontend:
   1. install packages under fronted directory (`npm install`)
   2. run app in development (`npm start`)
   3. build app for production (`npm build`)

### Prerequisites

Softwares that are needed to be installed are: \

1. python v3.10+
2. Node.js v15+ for frontend setup

```
Give examples
```

### Installing

For Development, create a .env file with following: \

1. PORT = `<specify the port number to run app on>`
2. HOST = `<specify the host to run app on>`
3. DEBUG = `<to turn debug on for development>`

## 🚀 Deployment <a name = "deployment"></a>

- **Heroku**

## ✍️ Authors <a name = "authors"></a>

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- ONDC
