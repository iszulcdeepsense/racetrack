from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


class JobEntrypoint:

    def webview_app(self, base_url: str):
        """
        Create ASGI app serving custom UI pages
        :param base_url Base URL prefix where WSGI app is deployed.
        """
        app = FastAPI()

        @app.get('/')
        async def _index(request: Request):
            return RedirectResponse(f"{base_url}/static/Quake3.htm")

        app.mount("/static", StaticFiles(directory="static"), name="static")

        return app
