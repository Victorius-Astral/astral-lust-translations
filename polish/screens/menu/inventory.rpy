# TODO: Translation updated at 2024-10-17 01:25

translate polish strings:

    # game/screens/menu/inventory.rpy:50
    old "Character"
    new "Postać" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:50
    old "Craft"
    new "Rzemiosło" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"
    new "{b}{u}{color=#d26a6a}Zdrowie{/color}{/u}{/b}\n{small}Ilość obrażeń, które możesz przyjąć.{/small}\n\n{b}{u}{color=#C6E2FF}Duchowość{/color}{/u}{/b}\n{small}Zużywana podczas używania kart w walce. Odnawia się na początku nowej tury.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"
    new "{b}{u}{color=#DAD1BF}Poczytalność{/color}{/u}{/b}\n{small}Jak bardzo jesteś zdolny do logicznego myślenia. Osiągnięcie 0% prowadzi do końca gry.{/small}\n\n{b}{u}{color=#800080}Zepsucie{/color}{/u}{/b}\n{small}Jak bardzo jesteś zdegenerowany. Osiągnięcie 100% prowadzi do końca gry.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"
    new "{b}{u}{color=#F4C25E}Siła{/color}{/u}{/b}\n{small}Zwiększa obrażenia zadawane w walce o 1 co 5 punktów.{/small}\n\n{b}{u}{color=#32CD32}Zręczność{/color}{/u}{/b}\n{small}Każdy punkt daje 1% unikania obrażeń i zwiększa szansę na ucieczkę z walki o 2%.{/small}\n\n{b}{u}{color=#A71930}Witalność{/color}{/u}{/b}\n{small}Każdy punkt zwiększa maksymalne zdrowie o 3.{/small}\n\n{small}Zwiększane na siłowni.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"
    new "{b}{u}{color=#B29EC1}Inteligencja{/color}{/b}{/u}\n{small}Używana w niektórych testach.{/small}\n\n{b}{u}{color=#C6E2FF}Mądrość{/color}{/b}{/u}\n{small}Każde 10 punktów zwiększa maksymalną duchowość o 1 punkt.{/small}\n\n{b}{u}{color=#FF958F}Charyzma{/color}{/b}{/u}\n{small}Używana w wielu testach. Używana do przekonywania innych w rozmowie.{/small}\n\n{small}Zwiększana w pokoju gracza.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:60
    old "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"
    new "{b}{u}{color=#E4CA48}Szczęście{/color}{/b}{/u}\n{small}Zwiększa szansę na dobre karty, zmniejsza szansę na spotkanie silnych przeciwników. Zwiększane kodami z Discorda lub poprzez handel z niektórymi istotami.{/small}" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:117
    old "State"
    new "Stan" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:128
    old "Health:\nSanity:\nCorruption:"
    new "Zdrowie:\nPoczytalność:\nZepsucie:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:129
    old "[player.hp]/[player.hp_max]\n[player.sanity]%\n[player.corruption]%"
    new "[player.hp]/[player.hp_max]\n[player.sanity]%\n[player.corruption]%" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:134
    old "Physical Stats"
    new "Statystyki fizyczne" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:145
    old "Strength:\nAgility:\nVitality:"
    new "Siła:\nZręczność:\nWitalność:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:146
    old "[player.strength]\n[player.agility]\n[player.vitality]"
    new "[player.strength]\n[player.agility]\n[player.vitality]" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:151
    old "Mental Stats"
    new "Statystyki mentalne" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:162
    old "Intelligence:\nWisdom:\nCharisma:"
    new "Inteligencja:\nMądrość:\nCharyzma:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:163
    old "[player.intelligence]\n[player.wisdom]\n[player.charisma]"
    new "[player.intelligence]\n[player.wisdom]\n[player.charisma]" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:168
    old "Other"
    new "Inne" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:179
    old "Luck:"
    new "Szczęście:" # TL # Victorius - AI

    # game/screens/menu/inventory.rpy:180
    old "[player.luck]"
    new "[player.luck]"

