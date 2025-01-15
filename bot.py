import nonebot
from nonebot.adapters.telegram import Adapter as TGAdapters
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)
driver.register_adapter(TGAdapters)


nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()
