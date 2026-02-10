[app]
# (str) Title of your application
title = Bashir GSM Pro V3

# (str) Package name
package.name = bashirgsmpro

# (str) Package domain
package.domain = com.bashir.v3

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (سطر واحد يجمع كل الملفات لمنع التكرار)
source.include_exts = py,png,jpg,kv,sh

# (str) Application version
version = 3.0

# (list) Application requirements
requirements = python3,kivy,android,usbserial

# (str) Icon filename (تأكد من وجود الملف icon.png في GitHub)
icon.filename = icon.png

# (str) Supported orientations
orientation = portrait

# (list) Permissions needed for GSM and File access
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, USB_PERMISSION, MANAGE_EXTERNAL_STORAGE

# (int) Android API to use (Targeting Android 13)
android.api = 33

# (int) Minimum API support (Android 5.0)
android.minapi = 21

# (str) Android NDK version to use (النسخة المستقرة التي نستخدمها)
android.ndk = 25b

# (bool) Use the screen's full height
fullscreen = 1

# (str) Android logcat filters for debugging
android.logcat_filters = *:S python:D
