[app]

# Название приложения
title = FoodOptionsApp

# Имя пакета
package.name = foodoptions

# Домен (можно любой)
package.domain = org.test

# Главный файл приложения
source.dir = .
source.include_exts = py

# Основной Python-файл
main.py

# Версия
version = 0.1

# Требуемые библиотеки
requirements = python3,kivy,openssl,libffi
android.api = 33
android.ndk = 25b
android.minapi = 21
android.archs = arm64-v8a
# Разрешения Android (минимально)
android.permissions = INTERNET

# Архитектуры
android.archs = arm64-v8a, armeabi-v7a

# Формат сборки
package.format = apk


[buildozer]
log_level = 2
warn_on_root = 1

