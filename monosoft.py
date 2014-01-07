import sublime, sublime_plugin
import os

template = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>author</key>
    <string>Domenico Carbotta - modified by Andy VanEe</string>
    <key>name</key>
    <string>IDLE-darksoft</string>
    <key>settings</key>
    <array>
        <dict>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string>##BG##</string>
                <key>caret</key>
                <string>##FG##</string>
                <key>foreground</key>
                <string>##FG##</string>
                <key>invisibles</key>
                <string>##HH##10</string>
                <key>lineHighlight</key>
                <string>##HH##15</string>
                <key>selection</key>
                <string>##HH##15</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Comment</string>
            <key>scope</key>
            <string>comment</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##FG##70</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>String</string>
            <key>scope</key>
            <string>string</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##CC</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Number</string>
            <key>scope</key>
            <string>constant.numeric</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##CC</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Built-in constant</string>
            <key>scope</key>
            <string>constant.language</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##B0</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>User-defined constant</string>
            <key>scope</key>
            <string>constant.character, constant.other</string>
            <key>settings</key>
            <dict/>
        </dict>
        <dict>
            <key>name</key>
            <string>Variable</string>
            <key>scope</key>
            <string>variable.language, variable.other</string>
            <key>settings</key>
            <dict/>
        </dict>
        <dict>
            <key>name</key>
            <string>Keyword</string>
            <key>scope</key>
            <string>keyword</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##B0</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Storage</string>
            <key>scope</key>
            <string>storage</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##B0</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Type name</string>
            <key>scope</key>
            <string>entity.name.type</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##CC</string>
                <key>fontStyle</key>
                <string>bold</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Inherited class</string>
            <key>scope</key>
            <string>entity.other.inherited-class</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##87</string>
                <key>fontStyle</key>
                <string>bold</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Function name</string>
            <key>scope</key>
            <string>entity.name.function</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##FF</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Function argument</string>
            <key>scope</key>
            <string>variable.parameter</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##9F</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Tag name</string>
            <key>scope</key>
            <string>entity.name.tag</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##FG##9F</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Tag attribute</string>
            <key>scope</key>
            <string>entity.other.attribute-name</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##FG##9F</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library function</string>
            <key>scope</key>
            <string>support.function</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##AC</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library constant</string>
            <key>scope</key>
            <string>support.constant</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##AC</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library class/type</string>
            <key>scope</key>
            <string>support.type, support.class</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##CF</string>
                <key>fontStyle</key>
                <string>bold</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library variable</string>
            <key>scope</key>
            <string>support.variable</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>##HH##EF</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Invalid</string>
            <key>scope</key>
            <string>invalid</string>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string>##HH##6F</string>
                <key>foreground</key>
                <string>#A0A9AFFF</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>String interpolation</string>
            <key>scope</key>
            <string>constant.other.placeholder.py</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string></string>
                <key>foreground</key>
                <string>##HH##BF</string>
            </dict>
        </dict>
    </array>
    <key>uuid</key>
    <string>DDC0CBE1-442B-4CB5-80E4-26E4CFB3A277</string>
</dict>
</plist>
'''

PLUGIN_FOLDER = os.path.dirname(os.path.realpath(__file__))
SETTINGS_FILE = "monosoft.sublime-settings"
DEFAULT_SETTINGS = ['#222222', '#CCCCCC', '#555555']

def hex2rgb(color):
    color = color.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in range(0, 6, 2))

def mix(colorA, colorB, percent):
    a_rgb = hex2rgb(colorA)
    b_rgb = hex2rgb(colorB)
    c_rgb = (0,0,0)
    c_rgb[0] = ((a_rgb[0] * percent) + b_rgb[0]) / percent
    return colorA

def match_hex(color):
    '''This should be better'''
    return len(color) == 7

def write_file():
    settings = sublime.load_settings(SETTINGS_FILE)
    fg = settings.get('monosoft-foreground')
    bg = settings.get('monosoft-background')
    hh = settings.get('monosoft-highlight')

    if match_hex(fg) and match_hex(bg) and match_hex(hh):
        pass
    else:
        fg, bg, hh = DEFAULT_SETTINGS
        sublime.status_message('Invalid monosoft settings')

    with open(sublime.packages_path()+'/monosoft/monosoft.tmTheme', 'w') as f:
        t = template
        t = t.replace('##FG##', fg)
        t = t.replace('##BG##', bg)
        t = t.replace('##HH##', hh)
        sublime.status_message('theme file updated')
        f.write(t)

def plugin_loaded():
    '''Only runs properly in ST3?'''
    settings = sublime.load_settings(SETTINGS_FILE)
    settings.add_on_change('monosoft-foreground', write_file)
    settings.add_on_change('monosoft-background', write_file)
    settings.add_on_change('monosoft-highlight', write_file)

class MonosoftCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        write_file()

class MonosoftEditColors(sublime_plugin.TextCommand):
    def run(self, edit):
        monosoft_edit_color_scheme(self.view.window())

def monosoft_edit_color_scheme(window):
    settings_file = os.path.join(PLUGIN_FOLDER, SETTINGS_FILE)
    window.open_file(settings_file)
