import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from src.web.controller.controlador_web import ControladorWeb

if __name__ == "__main__":
    app = FastAPI()
    controlador_web = ControladorWeb()
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(controlador_web.router)
    app.mount("/", StaticFiles(directory="src/web", html=True), name="static")
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
