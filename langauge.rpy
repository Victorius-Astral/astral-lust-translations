define available_languages = OrderedDict()
default persistent.show_hidden_languages = False

init python:

    # image, language name, language ID, completion %, Public
    available_languages[None] = ("united-states", _("English"), "100%", True)
    available_languages["spanish"] = ("spain", _("Spanish"), "100%", True)
    available_languages["french"] = ("france", _("French"), "99.9%\nCommunity", True)
    available_languages["vietnamese"] = ("vietnam", _("Vietnamese"), "100%\nCommunity", True)
    available_languages["polish"] = ("poland", _("Polish"), "3%", False)
    available_languages["chinese"] = ("china", _("Chinese"), "5%\nCommunity", False)
