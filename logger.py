import logging # Модуль для ведения логов

# Создаём конфигурацию логирования
logging.basicConfig(
    filename="app.log",          # файл для логирования
    level=logging.INFO,          # уровень логирования (фильтр сообщений)
    format="%(asctime)s - %(levelname)s - %(message)s", # формат записи логов
    encoding="utf-8"             # кодировка файла
)

logger = logging.getLogger("app_logger") # создание логгера с именем "app_logger"