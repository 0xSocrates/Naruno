[app]
title = Naruno
package.name = naruno
package.domain = org.naruno
source.dir = naruno/
source.include_exts = py,png,jpg,kv,atlas
version = 0.44.4
orientation = landscape
fullscreen = 0
android.permissions = INTERNET
icon.filename = naruno/gui_lib/images/logo.ico
presplash.filename = naruno/gui_lib/images/logo.png
android.presplash_color = black
p4a.local_recipes = recipes/src/python-for-android/recipes/
android.api = 27

[app@api]
title = Naruno-API
package.name = naruno_api
source.dir = naruno/api/buildozer/
requirements =  naruno==0.44.4, Kivy==2.1.0, waitress==2.1.2, werkzeug==2.0.3, flask==2.0.0, flask_cors==3.0.10

[app@gui]
title = Naruno-GUI
package.name = naruno_gui
source.dir = naruno/gui/
requirements =  naruno==0.44.4, Kivy==2.1.0, kivymd==0.104.2, qrcode==7.3.1, kivymd_extensions.sweetalert==0.1.5, plyer==2.1.0, pillow==9.1.1




[buildozer]
log_level = 2
warn_on_root = 1
