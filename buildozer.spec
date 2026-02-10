[app]
title = Bashir GSM Pro V3
package.name = bashirgsmpro
package.domain = com.bashir.v3
source.dir = .
source.include_exts = py,png,jpg,kv,sh
version = 3.0
requirements = python3,kivy,android,usbserial
icon.filename = icon.png
orientation = portrait
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, USB_PERMISSION, MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
fullscreen = 1
android.logcat_filters = *:S python:D

