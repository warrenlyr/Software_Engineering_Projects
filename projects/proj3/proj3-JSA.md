# proj3-JSA

Vocabulary anagrams game for primary school English language learners (ELL)

Author: Warren Liu

## Overview

A simple anagram game designed for English-language learning students in elementary and middle school. Students are presented with a list of vocabulary words (taken from a text file) and an anagram. The anagram is a jumble of some number of vocabulary words, randomly chosen. Students attempt to type words that can be created from the jumble. When a matching word is typed, it is added to a list of solved words.

The vocabulary word list is fixed for one invocation of the server, so multiple students connected to the same server will see the same vocabulary list but may have different anagrams.

## Authors

Initial version by M Young; Docker version added by R Durairajan; to be revised by CIS 322 students.

## Status

flask_vocab.py and the template vocab.html are a 'skeleton' version of the anagram game for a CIS 322 project. They uses conventional interaction through a form, interacting only when the user submits the form.

## Minijax?

flask_minijax.py and templates/minijax.html are a tiny example of using JQuery with flask for an Ajax application. They should not be included in the version of the project you turn in.

## Tasks

- Familiarize yourself with flask_vocab.py and flask_minijax.py by running them separately. You need to understand them to do this project.

- Your task is to replace the form interaction (in flask_vocab.py) with AJAX interaction on each keystroke using flask_minijax.py.

- You will write your own Dockerfile (see examples provided in prior projects). Dockerfile should be placed inside vocab folder.

- You will submit your credentials.ini in canvas. It should have information on how we should get your git repo (which should contain your Dockerfile).

## Use

```
./run.sh
```
OR
```
docker build -t <name> .
docker run -d -p 5000:5000 <name>
```