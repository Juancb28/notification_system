from api import api


def start():
    import uvicorn
    uvicorn.run('api.api:app', host='127.55.55.55', port=5757, reload=True)

if __name__ == "__main__":
    start()
