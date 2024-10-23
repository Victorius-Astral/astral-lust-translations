# TODO: Translation updated at 2024-10-20 16:20

translate german strings:

    # game/screens/menu/inventory.rpy:50
    old "Character"
    new "Charakter" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:50
    old "Craft"
    new "Handwerk" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"
    new "{b}{u}{color=#d26a6a}Gesundheit{/color}{/u}{/b}\n{small}Wie viel Schaden du ertragen kannst.{/small}\n\n{b}{u}{color=#C6E2FF}Spiritualität{/color}{/u}{/b}\n{small}Wird beim Einsatz von Karten im Kampf verbraucht. Erholt sich zu Beginn einer neuen Runde.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"
    new "{b}{u}{color=#DAD1BF}Verstand{/color}{/u}{/b}\n{small}Wie fähig du zu logischem Denken bist. Erreicht 0%% führt zum Spielende.{/small}\n\n{b}{u}{color=#800080}Korruption{/color}{/u}{/b}\n{small}Wie degeneriert du bist. Erreicht 100%% führt zum Spielende.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"
    new "{b}{u}{color=#F4C25E}Stärke{/color}{/u}{/b}\n{small}Erhöht den im Kampf verursachten Schaden um 1 für alle 5 Punkte.{/small}\n\n{b}{u}{color=#32CD32}Beweglichkeit{/color}{/u}{/b}\n{small}Jeder Punkt gibt 1%% Vermeidung von Schaden und erhöht die Chance, dem Kampf zu entkommen, um 2%%.{/small}\n\n{b}{u}{color=#A71930}Vitalität{/color}{/u}{/b}\n{small}Jeder Punkt erhöht deine maximale Gesundheit um 3.{/small}\n\n{small}Im Fitnessstudio erhöht.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"
    new "{b}{u}{color=#B29EC1}Intelligenz{/color}{/b}{/u}\n{small}Wird bei einigen Prüfungen verwendet.{/small}\n\n{b}{u}{color=#C6E2FF}Weisheit{/color}{/b}{/u}\n{small}Alle 10 Punkte erhöhen die maximale Spiritualität um 1 Punkt.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Wird in vielen Prüfungen verwendet. Wird genutzt, um andere im Gespräch von sich zu überzeugen.{/small}\n\n{small}Im Spielerzimmer erhöht.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"
    new "{b}{u}{color=#E4CA48}Glück{/color}{/b}{/u}\n{small}Erhöht die Chance auf gute Karten, verringert die Chance, auf starke Gegner zu treffen. Erhöht mit Codes von Discord oder durch Handel mit bestimmten Wesen.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:117
    old "State"
    new "Zustand" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:128
    old "Health:\nSanity:\nCorruption:"
    new "Gesundheit:\nVerstand:\nKorruption:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:129
    old "[player.hp]/[player.hp_max]\n[player.sanity]%\n[player.corruption]%"
    new "[player.hp]/[player.hp_max]\n[player.sanity]%%\n[player.corruption]%%" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:134
    old "Physical Stats"
    new "Physische Werte" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:145
    old "Strength:\nAgility:\nVitality:"
    new "Stärke:\nBeweglichkeit:\nVitalität:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:146
    old "[player.strength]\n[player.agility]\n[player.vitality]"
    new "[player.strength]\n[player.agility]\n[player.vitality]" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:151
    old "Mental Stats"
    new "Mentale Werte" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:162
    old "Intelligence:\nWisdom:\nCharisma:"
    new "Intelligenz:\nWeisheit:\nCharisma:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:163
    old "[player.intelligence]\n[player.wisdom]\n[player.charisma]"
    new "[player.intelligence]\n[player.wisdom]\n[player.charisma]" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:168
    old "Other"
    new "Sonstiges" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:179
    old "Luck:"
    new "Glück:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:180
    old "[player.luck]"
    new "[player.luck]"

