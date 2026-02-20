from fastapi import FastAPI
from routes.api_news import router as news_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='API Notification System', version='0.0.1')

app.include_router(news_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


