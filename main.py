#!/usr/bin/env python

import wikipedia
import random

random_article = wikipedia.random()
page = wikipedia.page(random_article)

print(page.title)
print(page.summary)
print(page.content)
