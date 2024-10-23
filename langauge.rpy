define available_languages = OrderedDict()
default persistent.show_hidden_languages = False

init python:

    # langauge, translated language
    available_languages[None] = ("English", "English")
    available_languages["spanish"] = ("Spanish", "Español")
    available_languages["french"] = ("French", "Français")
    available_languages["vietnamese"] = ("Vietnamese", "Tiếng Việt")
    available_languages["polish"] = ("Polish", "Polski")
    available_languages["chinese"] = ("Chinese (Simplified)", "{font=fonts/NotoSerifSC-Regular.otf}中文 (简体){/font}")
    available_languages["chinese_traditional"] = ("Chinese (Traditional)", "{font=fonts/NotoSerifSC-Regular.otf}中文 (繁體){/font}")
    available_languages["italian"] = ("Italian", "Italiano")
    available_languages["portuguese"] = ("Portuguese", "Português")
    available_languages["german"] = ("German", "Deutsch")

    def getLanguage():
        global available_languages

        try:
            return available_languages[_preferences.language]

        except KeyError:
            renpy.change_language(None, True)
            return available_languages[None]

init -1 python:
    def restoreFonts():
        global fonts
        global gui

        fonts_init()
        victorius.who_args["font"] = fonts["nanum_pen"]
        victorius.what_args["font"] = fonts["nanum_pen"]

        fonts["noto_serif_sc"] = "fonts/NotoSerifSC-Regular.otf"
        fonts["itim"] = "fonts/Itim-Regular.ttf"
        fonts["brygada"] = "fonts/Brygada1918-Regular.ttf"

        gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = fonts["itim"]

    def overrideFont(font):
        global gui
        gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = font

translate None python:
    restoreFonts()

translate vietnamese python:
    restoreFonts()

    fonts["nanum_pen"] = fonts["brygada"]
    fonts["bodoni"] = fonts["brygada"]
    victorius.who_args["font"] = fonts["brygada"]
    victorius.what_args["font"] = fonts["brygada"]

translate spanish python:
    restoreFonts()

    fonts["nanum_pen"] = fonts["brygada"]
    victorius.who_args["font"] = fonts["brygada"]
    victorius.what_args["font"] = fonts["brygada"]

translate chinese python:
    restoreFonts()
    fonts["brygada"] = fonts["noto_serif_sc"]
    fonts["itim"] = fonts["noto_serif_sc"]
    overrideFont(fonts["noto_serif_sc"])

translate chinese_traditional python:
    restoreFonts()
    fonts["brygada"] = fonts["noto_serif_sc"]
    fonts["itim"] = fonts["noto_serif_sc"]
    overrideFont(fonts["noto_serif_sc"])


translate polish python:
    restoreFonts()

    fonts["philosopher"] = fonts["brygada"]
    fonts["noto_serif_sc"] = fonts["brygada"]
    fonts["fredericka"] = fonts["brygada"]
