[app]

# Название приложения
title = FoodOptionsApp

# Имя пакета
package.name = foodoptions

# Домен (любое значение)
package.domain = org.test

# Корневая папка и файлы приложения
source.dir = .
source.include_exts = py

# Главный файл
main.py

# Версия
version = 0.1

# Python-библиотеки
requirements = python3,kivy,openssl,libffi

# Настройки Android
android.api = 33
android.ndk = 25b
android.minapi = 21

# Архитектуры (всего ОДИН раз!)
android.archs = arm64-v8a, armeabi-v7a

# Разрешения
android.permissions = INTERNET

# Формат сборки
package.format = apk


[buildozer]
log_level = 2
warn_on_root = 1
