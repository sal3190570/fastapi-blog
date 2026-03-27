from fastapi import FastAPI, HTTPException, status, Request

from fastapi.templating import Jinja2Templates
app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts:list[dict] = [
    {
        "id": 1,
        "author": "Salman Awal",
        "title": "FastAPI is cool",
        "content": "This framework is easy to use",
        "date_posted": "March 24, 2026" 
    },
    {
        "id": 2,
        "author": "Matt Palombo",
        "title": "Python is cool",
        "content": "This language is easy to use",
        "date_posted": "March 24, 2026" 
    },
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"request": request, "title": "Sal", "posts": posts},
    )




@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{id}", status_code=status.HTTP_200_OK)
def get_post_by_id(id: int):
    for post in posts:
        if post["id"] == id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")  