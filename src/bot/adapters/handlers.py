import abc

from src.bot.adapters.message import AbstractBusMessage


class AbstractHandler(abc.ABC):
    @abc.abstractmethod
    async def handle(self, message: AbstractBusMessage):
        raise NotImplementedError
