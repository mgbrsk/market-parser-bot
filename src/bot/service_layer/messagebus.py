from src.bot.adapters.handlers import AbstractHandler
from src.bot.adapters.message import AbstractBusMessage
import asyncio


class MessageBus:
    def __init__(self):
        self.queue: list[AbstractBusMessage] = []
        self.handlers: list[AbstractHandler] = []

    async def handle(self, message: AbstractBusMessage):
        self.queue.append(message)
        for handler in self.handlers:
            await handler.handle(self.queue.pop(0))

    async def register(self, handler: AbstractHandler):
        self.handlers.append(handler)

    async def start(self) -> None:
        await asyncio.gather(*[h.start() for h in self.services])

    async def stop(self) -> None:
        for h in self.services:
            await h.stop()
