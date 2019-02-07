import logging; logging.basicConfig(level=logging.INFO)
from aiohttp import web


async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

if __name__ == '__main__':
    app = web.Application()
    app.router.add_route('GET', '/', index)
    logging.info('启动服务器：127.0.0.1:8000...')
    web.run_app(app, host='127.0.0.1', port=8000)
