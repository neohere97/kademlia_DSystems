import argparse
import asyncio
import logging
from aiohttp import web
from kademlia.network import Server
import time
import os
from multiprocessing import Process

number_of_nodes = 0  # global variable to store the number of nodes
base_port = 0

async def run(node, port, number_of_nodes,base_port):
    await node.listen(port)
    for i in range(base_port, port+1):
        await node.bootstrap([("0.0.0.0", i)])
        time.sleep(0.1);
   
        

async def set_key(request):
    node = request.app["node"]
    key = request.match_info.get("key", "")
    value = request.match_info.get("value", "")
    await node.set(key, value)
    return web.Response(text=f"Key '{key}' set to '{value}'")


async def get_key(request):
    node = request.app["node"]
    key = request.match_info.get("key", "")
    print(key);
    value = await node.get(key)
    return web.Response(text=f"Key '{key}' has value '{value}'")


async def serve_file(request):
    filename = request.match_info.get("filename", "")
    file_path = os.path.join(os.getcwd(), "flower_images", filename)
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
        return web.Response(body=file_content, content_type="application/octet-stream")
    except FileNotFoundError:
        return web.Response(status=404, text=f"File '{filename}' not found")


async def create_app(node):
    app = web.Application()
    app["node"] = node
    app.router.add_get("/get/{key}", get_key)
    app.router.add_get("/set/{key}/{value}", set_key)
    app.router.add_get("/file/{filename}", serve_file)
    return app


async def spawn_http_server(node, port):
    app = await create_app(node)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", port)
    await site.start()


async def spawn_node(kademlia_port, http_port, number_of_nodes, base_port):
    print(f"Number of nodes: {number_of_nodes}")
    node = Server()
    run_task = asyncio.create_task(run(node, kademlia_port, number_of_nodes, base_port))
    http_task = asyncio.create_task(spawn_http_server(node, http_port))
    wait_task = asyncio.create_task(asyncio.sleep(3600))
    try:
        await asyncio.gather(run_task, http_task, wait_task)
    except KeyboardInterrupt:
        wait_task.cancel()
        await wait_task


def run_node_on_process(kademlia_port, http_port, number_of_nodes, base_port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(spawn_node(kademlia_port, http_port, number_of_nodes, base_port))



def main():
    global number_of_nodes
    global base_port

    parser = argparse.ArgumentParser(description="Spawn multiple Kademlia nodes.")
    parser.add_argument("N", type=int, help="The number of nodes to create.")
    parser.add_argument("base_port", type=int, help="The base port to start from.")
    parser.add_argument("base_port_http", type=int, help="The base port to start from.")
    args = parser.parse_args()

    number_of_nodes = args.N
    base_port = args.base_port
    base_port_http = args.base_port_http

    # Generate a list of ports for the Kademlia and HTTP instances
    kademlia_ports = [base_port + i for i in range(number_of_nodes)]
    http_ports = [base_port_http + i for i in range(number_of_nodes)]

    print("Kademlia ports ->", kademlia_ports)
    print("HTTP Kademlia ports ->", http_ports)

    # Spawn multiple instances of nodes, each in a separate process
    processes = [
        Process(
            target=run_node_on_process,
            args=(kademlia_port, http_port, number_of_nodes, base_port),
        )
        for kademlia_port, http_port in zip(kademlia_ports, http_ports)
    ]

    # Start the processes
    for process in processes:
        process.start()

    # Wait for processes to finish
    for process in processes:
        process.join()


if __name__ == "__main__":
    main()