from src.bot.adapters.handlers import AbstractHandler
from src.bot.adapters.message import AbstractBusMessage


class MessageBus:
    def __init__(self):
        self.queue: list[AbstractBusMessage] = []

    async def handle(self, message: AbstractBusMessage):
        self.queue.append(message)
