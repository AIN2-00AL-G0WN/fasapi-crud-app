import uvicorn
from fastapi import FastAPI
from app.routes.item import route as item_route
<<<<<<< HEAD

# setting up a Fastapi app
app=FastAPI()

# adding routes to our app
app.include_router(router=item_route,prefix='api')
=======
>>>>>>> 6e9f3c425ca12f7986660507d2d74155d9a3c117

# setting up a Fastapi app
app=FastAPI()

# adding routes to our app
app.include_router(router=item_route,prefix='/api')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)