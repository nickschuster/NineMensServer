import asyncio
import time

ADDR = '192.168.0.64'
PORT = 12345
CLIENTS = []
TYPE = 'H'

async def serve(reader, writer):
	global TYPE
	global CLIENTS
	client = writer.get_extra_info('peername')
	CLIENTS.append(client)
	if TYPE == 'C':
		writer.write(TYPE.encode('utf-8'))
		writer.write(CLIENTS[index-1][0].encode('utf-8'))
		TYPE = 'H'
	else:
		writer.write(TYPE.encode('utf-8'))
		TYPE = 'C'
	
	if len(CLIENTS) == 2:
		CLIENTS = []

	await writer.drain()
	writer.close()
	await writer.wait_closed()

async def main():
    server = await asyncio.start_server(serve, ADDR, PORT)
    await server.serve_forever()

asyncio.run(main())
