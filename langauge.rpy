define available_languages = OrderedDict()
default persistent.show_hidden_languages = False

init python:

    # image, language name, language ID, completion %, Public
    available_languages[None] = ("united-states", _("English"), True)
    available_languages["spanish"] = ("spain", _("Spanish"), True)
    available_languages["french"] = ("france", _("French"), True)
    available_languages["vietnamese"] = ("vietnam", _("Vietnamese"), True)
    available_languages["polish"] = ("poland", _("Polish"), True)
    available_languages["chinese"] = ("china", _("Chinese"), False)

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

        gui.text_font = fonts["itim"]
        gui.name_text_font = fonts["itim"]
        gui.interface_text_font = fonts["itim"]

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


translate polish python:
    restoreFonts()

    fonts["philosopher"] = fonts["brygada"]
    fonts["barcodeText"] = fonts["brygada"]
    fonts["noto_serif_sc"] = fonts["brygada"]
    fonts["fredericka"] = fonts["brygada"]
