from src.bot.service_layer.messagebus import MessageBus


def bootstrap() -> MessageBus:
    return MessageBus()
