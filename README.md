# VK to Discord

**Показывает текущую проигрываемую песню, как активность в Discord.**  
(*Display your current listen to a song from VK status.*)

## Установка (Installation)

1. **Клонируем репозиторий** (*Clone repository*)

    ```bash
    git clone https://github.com/TheDarkFireDesu/VKToDiscord-Python.git
    ```

2. **Переходим в папку с репозиторием** (*Go to VKToDiscord-Python folder*)

    ```bash
    cd VKToDiscord-Python
    ```

3. **Установливаем зависимости при помощью pip** (*Install libraries using pip*)

    ```bash
    pip install -r requirements.txt
    ```

## Настройка (Setting up)

1. **Заполним файл конфигурации settings.py** (*Fill in the config*)

    ```json
    {
        "id": "",
        "app_id": "",
        "app_token": "",
        "language": ""
    }
    ```

2. **Получение ID**

    - Переходи на свою страницу ВК.
    - Заходим в свой профиль.
    - Копируем из адресной строки свой ID (*example: user293932 или dkawdkoe*).
    - Вставляем в поле id, сохраняя кавычки.

3. **Получение APP_ID**

    - Переходим в Dashboard Discord: [link](https://discord.com/developers/applications)
    - Создаем приложение.
    - Копируем Application ID.
    - Вставляем в поле app_id.

4. **Получение APP_TOKEN**

    - Переходим в «для разработчиков» в ВК: [link](https://dev.vk.com)
    - Создаем приложение.
    - В настройках приложения ищем поле «Сервисный ключ доступ».
    - Копируем его.
    - Вставляем в поле app_token.

5. **Изменение локализации**

    Локализация поддерживается посредством JSON. Обязательны для заполнения поля state, title, artist. (Русский = ru-RU)

    ```json
    {
        "language": "",
        "author": "",
        "link": "",

        "state": "",
        "title": "",
        "artist": ""
    }
    ```

## Запуск (Start)

```bash
python main.py
```

## ЧаВО (FAQ)

1. **Библиотеки** (*Used libraries*)
    - vk_api
        - [github.com](https://github.com/python273/vk_api)
    - pypresence
        - [github.com](https://github.com/qwertyquerty/pypresence)

2. **Отличия от оригинала** (Diffences from original)
    - Отсутствие configparser, chardet, виртуального окружения, захардкоженного app_id, если не хотите, используйте app_id автора оригинала - "543726720289734656"
    - Поддержка локализации и настроек через JSON, логгирование.

3. **Авторство** (*Credits*)
    - [D3rise](https://github.com/D3rise) - автор оригинала.
    - [d1rknwh1te3](https://github.com/d1rknwh1te3) - скромнейший форкнувший чел.
