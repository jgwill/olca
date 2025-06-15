import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send("ACK")

def main():
    start_server = websockets.serve(echo, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket server running on ws://localhost:8765")
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
