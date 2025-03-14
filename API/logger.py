import sys
from loguru import logger


logger.remove()
logger.add(sink=sys.stdout, format="<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
                                   " | <level>{level: <8}</level>"
                                   " | <cyan><b>{line}</b></cyan>"
                                   " - <white><b>{message}</b></white>")
logger = logger.opt(colors=True)

# # Пример логирования
# logger.debug("Это отладочное сообщение.")  # Синий
# logger.info("Информационное сообщение.")   # Белый
# logger.success("Успешное выполнение!")     # Зелёный
# logger.warning("Предупреждение!")          # Жёлтый
# logger.error("Ошибка!")                    # Красный
# logger.critical("Критическая ошибка!")     # Малиновый
