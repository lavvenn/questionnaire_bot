from fastapi import FastAPI

from data.db import get_user_data

app = FastAPI(
    title='WebApp',
)

@app.get('/profile/{user_id}')
def get_profile(user_id: int):
    user_data = get_user_data(user_id)

    return user_data