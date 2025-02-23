import abc

from src.bot.adapters import message
from src.bot.domain.model import MessageToUser


class AbstractHandler(abc.ABC):
    @abc.abstractmethod
    async def handle(self, message: message.AbstractBusMessage):
        raise NotImplementedError


class SearchHandler(AbstractHandler):
    async def handle(self, message: message.SearchRequest):
        pass


class TelegramHandler(AbstractHandler):
    async def handle(self, message: message.AbstractBusMessage):
        pass

    async def send_message(self, message: MessageToUser):
        pass
