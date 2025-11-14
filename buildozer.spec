[app]

title = FoodOptionsApp
package.name = foodoptions
package.domain = org.test

source.dir = .
source.include_exts = py
main.py

version = 0.1

requirements = python3,kivy,openssl

android.api = 33
android.minapi = 21

# Архитектуры
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET
package.format = apk

[buildozer]
log_level = 2
warn_on_root = 1
