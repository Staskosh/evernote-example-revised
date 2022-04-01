# Работа с заметками Evernote
Данный скрипт позволяет работать с заметками [Evernote](https://evernote.com/intl/ru) 


### Как установить

Зарегистрируйтесь на [сайте](https://www.evernote.com/Registration.action?referralSpecifier=mktgrepack_en_oo_web_cpl_V00).
Введите свои данные по [ссылке](https://dev.evernote.com/#apikey) для получения `Consumer Key` и `Consumer Secret`.
Получите персональный токен по [ссылке](https://dev.evernote.com/support/glossary.php#k.

Далее рядом с кодом вы должны создать файл `.env`, в котором будут храниться
ваши личные данные:

```
EVERNOTE_CONSUMER_KEY='Тут ваш Consumer Key'
EVERNOTE_CONSUMER_SECRET='Тут ваш Consumer Secret'
EVERNOTE_PERSONAL_TOKEN='Тут ваш токен'
```

[Python3](https://www.python.org/downloads/) и [виртуальное окружение](https://python-scripts.com/virtualenv) должны быть установлены.
### Как запустить
1. Скачайте код
2. Установите зависимости командой:
```bash
pip install -r requirements.txt
```
3. Запустите скрипт:
```bash
python3 list_notebooks.py
```
Вы получите GUID и Название ваших блокнотов. 
4. В файл `.env` вставьте:
```
INBOX_NOTEBOOK_GUID='Тут полученный GUID из list_notebooks.py'
```
5. Запустите скрипт для отображения в консоли всех заметок из выбранного блокнота:
По умолчанию показываются только 10 последних. Вы можете выбрать другое количество указав количество при запуске.
```bash
python3 dump_inbox.py 'тут можно указать кол-во заметок'
```
6. Если вы хотите добавить новую заметку, то воспользуйтесь следующим скриптом:

Перед запуском выберете заметку как шаблон и укажите в файле `.env` ее GUID.
```
JOURNAL_TEMPLATE_NOTE_GUID='Тут GUID шаблонной заметки'
```
Также, укажите GUID блокнота, где вы хотите создать заметку.
```
JOURNAL_NOTEBOOK_GUID='Тут GUID блокнота'
```
По умолчанию в название новой заметки будет добавлена текущая дата и день.
Вы можете изменить дату при запуске скрипта.
```bash
python3 add_note2journal.py 'тут можно указать дату'
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org).
