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
