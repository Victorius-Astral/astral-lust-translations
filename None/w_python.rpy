init -1 python:
    def restoreFonts():
        global fonts

        fonts_init()
        victorius.who_args["font"] = fonts["nanum_pen"]
        victorius.what_args["font"] = fonts["nanum_pen"]

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

    fonts["itim"] = fonts["brygada"]

translate polish python:
    restoreFonts()

    fonts["philosopher"] = fonts["brygada"]
    fonts["barcodeText"] = fonts["brygada"]
    fonts["noto_serif_sc"] = fonts["brygada"]
    fonts["fredericka"] = fonts["brygada"]
