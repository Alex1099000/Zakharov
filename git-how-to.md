#Инструкция
## Создаем ssh-ключ:

1. Скачать и открыть *git-bush*.
2. Ввести команду `ssh-keygen -t ed25519 -C "your_email>@example.com"`.
3. Пара приватый-публичный ключ создана. С помощью команд `eval "$(ssh-agent -s)"` и `ssh-add <key_name>` добавить ключ в ssh-агент.

## Добавляем публичный ключ в аккаунт _GitHub_:

1. Зайти в раздел **Settings — SSH and GPG keys**.
2. Нажать **New SSH key**.
3. Задать ключу имя.
4. В поле со значением ввести данные, записанные в **<key_name>.pub**.
5. Нажать **New SSH key**.

## Клонируем репозиторий:

1. Зайти в (создать) репозиторий на *GitHub*.
2. Нажать **Code — SSH**. Скопировать ссылку.
3. Зайти в *git-bush*. С помощью команды `mkdir <path>/../<name>` создать директорию на компьютере.
4. Зайти в директорию, в которую мы будем копировать репозиторий с помощью команды `cd <path>/..`.
5. Ввести команду `git clone <SSH_link>`.
