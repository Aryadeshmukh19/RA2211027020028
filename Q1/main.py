from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware (Should now work properly)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Users Data
users = {
    "1": "John Doe",
    "2": "Jane Smith",
    "3": "Alice Johnson",
    "4": "Bob Williams",
    "5": "Marily Janes",
    "6": "Tom Holland",
    "7": "Jaden Styles",
    "8": "Emma Clarke",
    "9": "Elizabeth Johansson",
    "10": "Josh Smith",
}

# Top Users
top_users = {
    "1": "Jane Smith",
    "2": "Alice Johnson",
    "3": "John Doe",
    "4": "Josh Smith",
    "5": "Tom Holland",
}

# Popular Posts
popular_posts = [
    {"id": 1, "content": "This is a trending post!", "comments": 150, "likes": 1200},
    {"id": 2, "content": "React + FastAPI is amazing!", "comments": 120, "likes": 1100},
    {"id": 3, "content": "Today's visuals of the show were fire!", "commments": 100, "likes": 800},
]

# Routes
@app.get("/users")
def get_users():
    return {"users": users}

@app.get("/top_users")
def get_top_users():
    return {"top_users": top_users}

@app.get("/posts")
def get_posts(type: str):
    if type == "popular":
        return {"popular_posts": popular_posts}
    return {"error": "Invalid post type"}

@app.get("/")
def home():
    return {"message": "FastAPI Backend is Running!"}
