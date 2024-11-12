import uvicorn
from fastapi import FastAPI
from app.routes.item import route as item_route

# setting up a Fastapi app
app=FastAPI()

# adding routes to our app
app.include_router(router=item_route,prefix='/api')



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)