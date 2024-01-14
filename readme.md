# ephemerEx (ephemeral exchange)

Сервис для обмена приватными сообщениями, уничтожающимися после прочтения.
Получает текст сообщения в ручке /new и сохраняет его в базу, возвращая UUID записи.
В дальнейшем можно только один раз прочитать сообщение ручкой /read, передав в запросе UUID полученный в ответе /new.

# План развития
1. Очередь на чтение сообщений в виде Кафки
2. Эластик в виде хранилища отработанных сообщение
3. Тесты с использованием pytest
4. Нагрузочное тестирование с использованием locust
5. Мониторинг нагрузки с помощью Prometheus и Grafana


# Управление сервисом

### Запуск сервиса:
make up

### Настроенный Swagger, чтобы попробовать работу сервиса:
localhost:8080

### Потушить контейнеры и полностью зачистить образы:
make down
