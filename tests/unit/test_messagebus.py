import pytest

from bot.adapters.handlers import AbstractHandler
from src.bot.adapters.message import AbstractBusMessage
from src.bot.service_layer.messagebus import MessageBus


class FakeBusMessage(AbstractBusMessage):
    pass


@pytest.mark.asyncio
async def test_message_received_in_queue():
    message_bus = MessageBus()
    message: AbstractBusMessage = FakeBusMessage()
    await message_bus.handle(message)
    assert message_bus.queue == [message]
