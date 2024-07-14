from fastapi import FastAPI
from routers import auth_router, post_router

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(post_router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
