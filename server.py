import asyncio


ADDR = 'localhost'
PORT = 12345
CLIENTS = []

def serve(reader, writer):
	client = writer.get_extra_info('peername')
	CLIENTS.append(client)
	if len(CLIENTS) >= 2:
		print(CLIENTS[0], CLIENTS[1])
		del CLIENTS[0]
		del CLIENTS[0]



async def main():
    server = await asyncio.start_server(serve, ADDR, PORT)
    await server.serve_forever()

asyncio.run(main())
