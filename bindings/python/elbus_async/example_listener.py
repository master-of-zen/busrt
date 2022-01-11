import elbus_async
import asyncio


# frame handler
async def on_frame(frame):
    print('Frame:', hex(frame.type), frame.sender, frame.topic, frame.payload)


async def main():
    name = 'test.client.python.async'
    # create new elbus client and connect
    bus = elbus_async.client.Client('/tmp/elbus.sock', name)
    bus.on_frame = on_frame
    await bus.connect()
    # subscribe to all topics
    result = await bus.subscribe('#')
    print(hex(await result.wait_completed()))
    # wait for frames
    print(f'listening for messages to {name}...')
    while bus.is_connected():
        await asyncio.sleep(0.1)


asyncio.run(main())
