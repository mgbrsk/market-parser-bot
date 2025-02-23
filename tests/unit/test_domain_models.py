from src.bot.domain.model import MessageToUser
import pytest


def test_message_to_user():
    message = MessageToUser(chat_id=1, text="test message")
    assert message.chat_id == 1
    assert message.text == "test message"


def test_message_to_user_without_text():
    with pytest.raises(TypeError):
        MessageToUser(chat_id=1)  # type: ignore
