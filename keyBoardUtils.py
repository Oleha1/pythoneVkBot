from vkbottle import Keyboard, KeyboardButtonColor, Text


def getMainMenu():
    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Контакты", payload={"cmd": "contacts"}), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Доставка", payload={"cmd": "delivery"}), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("Ассортимент", payload={"cmd": "items"}), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("История компании", payload={"cmd": "info"}), color=KeyboardButtonColor.PRIMARY)
    ).get_json()
    return keyboard


def getBackMenu():
    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Назад", payload={"cmd": "menu"}), color=KeyboardButtonColor.SECONDARY)
    ).get_json()
    return keyboard
