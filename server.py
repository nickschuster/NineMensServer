import asyncio
import time
import struct

ADDR = '192.168.0.8'
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
		host = CLIENTS[0][0].split('.')
		writer.write(struct.pack('!B',int(host[0])))
		writer.write(struct.pack('!B',int(host[1])))
		writer.write(struct.pack('!B',int(host[2])))
		writer.write(struct.pack('!B',int(host[3])))
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
