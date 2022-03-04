define available_languages = [
    # image, language name, language ID, completion %
    ("spain", _("Spanish"), "spanish", "(98%)"),
    ("vietnam", _("Vietnamese"), "vietnamese", "(96%)"),

]

define gui.flag_size = (calc_gui(256), calc_gui(168))
transform flagIcon:
    xysize gui.flag_size

style languageSelector_text:
    xalign 0.5
    size gui.game_text
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style languageSelector_hbox:
    xcenter 0.5
    spacing gui.game_spacing_mini
    box_wrap True

screen language_selector():
    style_prefix "languageSelector"

    hbox:

        button:
            action Language(None), Confirm(_("Do you want to restart the game? If you don't do it, some things will not change language."), Function(renpy.quit, relaunch = True, save = True))

            vbox:
                add "united-states" at flagIcon
                text "English {#no-translate}"

        for lang in available_languages:

            button:
                action Language(lang[2]), Confirm(_("Do you want to restart the game? If you don't do it, some things will not change language."), Function(renpy.quit, relaunch = True, save = True))

                vbox:
                    add lang[0] at flagIcon
                    text lang[1]
                    text lang[3]
