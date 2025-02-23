from dataclasses import dataclass

from src.bot.adapters.message import AbstractBusMessage


@dataclass
class MessageToUser(AbstractBusMessage):
    chat_id: int
    text: str
