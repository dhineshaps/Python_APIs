from fastapi import FastAPI

app =FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/")
async def first_api():
  return{'Message' : "Hello Dhinesh"}

@app.get("/all-books")
async def first_api():
  return BOOKS

@app.get("/category/{cats}")
async def first_api_dy(cats):
  for cat in BOOKS:
    if cat["category"] == cats:
        return cat["title"]


@app.get("/category_title/{title}")  #http://127.0.0.1:8000/category_title/Title%20Three
async def first_api_dy(title):
  for cat in BOOKS:
    if cat["title"] == title:
        return cat["author"]
