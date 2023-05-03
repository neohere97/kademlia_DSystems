import os
import aiohttp
from aiohttp import web

async def serve_file(request):
    filename = request.match_info['filename']
    folder_path = './flower_images'  # Replace with the path to your folder
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        return aiohttp.web.FileResponse(file_path)
    else:
        raise web.HTTPNotFound()

app = web.Application()
app.router.add_route('GET', '/file/{filename}', serve_file)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
