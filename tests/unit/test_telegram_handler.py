import pytest
from src.bot.domain.model import MessageToUser
from src.bootstrap import bootstrap


class FakeTelegramMessageBroker:
    def __init__(self):
        self.sended_message = []

    async def send_message(self, message) -> None:
        self.sended_message.append(message)


@pytest.mark.asyncio
async def test_telegram_send_message_handler():
    message = MessageToUser(chat_id=1, text="test message")

    bus = bootstrap()
    await bus.handle(message)
