[app]

# Название приложения
title = FoodOptionsApp

# Имя пакета
package.name = foodoptions
package.domain = org.test

# Главный файл
source.dir = .
source.include_exts = py,kv,png,jpg,txt
main.py = main.py

# Версия приложения
version = 0.1

# Требуемые библиотеки
requirements = python3,kivy

# Android API
android.api = 33
android.minapi = 21

# NDK версия (строго поддерживаемая)
android.ndk = 25b

# Архитектуры сборки (рабочие)
android.archs = arm64-v8a, armeabi-v7a

# Разрешения
android.permissions = INTERNET

# Формат pakkета
package.format = apk


[buildozer]
log_level = 2
warn_on_root = 1
