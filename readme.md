# Как запустить бота?

Для запуска бота необходимо выполнить следующие действия

1. Создать виртуальное окружение

```sh
python3 -m venv env
```

2. Подключаем виртуальное окружение

```sh
. env/bin/activate
```

3. Устанавливаем зависимости

```
pip3 install -r requirements.txt
```

4. Запускаем бота

```
python3 main.py
```


# Как настроить бота?

1. Смена токена

```
Меня в .env файле константу BOT_API_TOKEN
```

2. Смена авторов

```
Меняем в .env файле константу AUTHORS (авторы через запятую)
```

3. Смена информационной картинки

```
Меняем в .env файле константу INFO_IMAGE и указываем там путь до картинки
```