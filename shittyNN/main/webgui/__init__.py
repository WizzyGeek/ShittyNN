import asyncio
import json
import json

from aiohttp import web
from pathlib import Path
from aiohttp_sse import sse_response

__all__ = (
    "make_app",
    "run_app",
)

async def index(_):
    return web.FileResponse(path=Path(__file__).parent / "static" / "index.html")

async def rec(req: web.Request):
    print(await req.json())
    req.app["eq"].put_nowait(100)
    return web.Response()

async def sse(req: web.Request):
    q = req.app["eq"]
    async with sse_response(req) as resp:
        while True:
            await resp.send(json.dumps(await q.get()), event="done")

async def make_app():
    app = web.Application()
    app.router.add_routes([web.get("/", index), web.post("/rec", rec), web.get("/sse", sse)])
    app.router.add_static("/static", Path(__file__).parent / "static")
    app["eq"] = asyncio.Queue()
    return app

def run_app_th(app):
    ...

run_app = web.run_app