[app]
# Charlie — standalone Android application
# Built specifically from charlie_fixed_android_ru.py

title = Charlie
package.name = charlie
package.domain = org.charlie
source.dir = .
source.include_exts = py,json,png,jpg,jpeg,atlas,kv,ttf,txt
version = 1.0.0

requirements = python3,kivy,numpy,pyjnius
orientation = portrait
fullscreen = 0

# Android runtime permissions used by Charlie.
# Android will ask the user when Charlie starts the sensors.
android.permissions = CAMERA,RECORD_AUDIO

# Stable Android toolchain used for this package.
android.minapi = 24
android.api = 35
android.ndk = 28c
android.ndk_api = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

# Kivy Android activity / storage.
android.entrypoint = org.kivy.android.PythonActivity
android.private_storage = True
android.app_name = Чарли
android.enable_androidx = True
android.debug_artifact = apk

# Keep the app window stable on modern phones.
android.allow_backup = True
android.logcat_filters = *:S python:D

# Pin python-for-android to the latest stable release currently published.
# This avoids pulling the active develop branch during the build.
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
