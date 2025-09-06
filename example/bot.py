import nonebot

# from nonebot.adapters.console import Adapter as ConsoleAdapter
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# from nonebot.adapters.satori import Adapter as SatoriAdapter


nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)
# driver.register_adapter(SatoriAdapter)

# nonebot.require("nonebot_plugin_alconna")
# nonebot.load_plugins("plugins")
nonebot.load_plugin("plugins.demo1")


async def _():
    from nonebot_plugin_alconna import Target, UniMessage, SupportScope

    await Target.group("123456789", SupportScope.qq_client).send(UniMessage.image(path="test.png"))


if __name__ == "__main__":
    nonebot.run()
