import uvicorn

from .app import app

def run():
    config = uvicorn.Config(app, port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
