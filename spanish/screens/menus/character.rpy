# TODO: Translation updated at 2021-05-17 12:56

translate spanish strings:

    # game/screens/menus/character.rpy:23
    old "{color=#FFD700}--- State ---{/color}"
    new "{color=#FFD700}--- Estado ---{/color}"

    # game/screens/menus/character.rpy:27
    old "{color=#A71930}Health{/color} - how much damage you can take.\n\n{color=#C6E2FF}Spirituality{/color} - consumed when using cards in combat. Recovers at the beginning of new turn."
    new "{color=#A71930}Salud{/color} - cuanto daño puede recibir.\n\n{color=#C6E2FF}Espiritualidad{/color} - consumido cuando se usan cartas en combate. Recuperado en nuevo turno"

    # game/screens/menus/character.rpy:31
    old "{color=#A71930}Health:{/color}\n{color=#C6E2FF}Spirituality:{/color}"
    new "{color=#A71930}Salud:{/color}\n{color=#C6E2FF}Espiritualidad:{/color}"

    # game/screens/menus/character.rpy:32
    old "{color=#A71930}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}"
    new "{color=#A71930}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}"

    # game/screens/menus/character.rpy:33
    old "\n{color=#FFD700}--- Mental State ---{/color}"
    new "\n{color=#FFD700}--- Estado Mental ---{/color}"

    # game/screens/menus/character.rpy:37
    old "{color=#DAD1BF}Sanity{/color} - how capable of logical reasoning you are. Reaching 0% leads to game over.\n\n{color=#800080}Corruption{/color} - how degenerated you are. Reaching 100% leads to game over."
    new "{color=#DAD1BF}Cordura{/color} - cuán capaz eres de razonar lógicamente. Llegar a 0% conduce al fin del juego.\n\n{color=#800080}Corrupción{/color} - lo degenerado que estás. Alcanzar 100% conduce al fin del juego."

    # game/screens/menus/character.rpy:41
    old "Sanity:\nCorruption:"
    new "Cordura:\Corrupción:"

    # game/screens/menus/character.rpy:42
    old "[player.sanity]%\n[player.corruption]%"
    new "[player.sanity]%\n[player.corruption]%"

    # game/screens/menus/character.rpy:43
    old "\n{color=#FFD700}--- Physical Stats ---{/color}"
    new "\n{color=#FFD700}--- Estadísticas Físicas ---{/color}"

    # game/screens/menus/character.rpy:47
    old "{color=#F4C25E}Strength{/color} - increases damage dealt in combat by 1 every 5 points.\n\n{color=#32CD32}Agility{/color} - every point gives 1% of avoiding damage and increases chance to escape combat by 2%.\n\n{color=#A71930}Vitality{/color} - every point increases your maximum health by 3.\n\nIncreased at the gym."
    new "{color=#F4C25E}Fuerza{/color} - incrementa daño por 1 cada 5 puntos en combate.\n\n{color=#32CD32}Agilidad{/color} - cada punto da 1% de evitar daño e incrementa oportunidades de escape por 2%.\n\n{color=#A71930}Vitalidad{/color} - cada punto incrementa tu salud por 3.\n\nIncrementada en gimnasio."

    # game/screens/menus/character.rpy:51
    old "Strength:\nAgility:\nVitality:"
    new "Fuerza:\nAgilidad:\nVitalidad:"

    # game/screens/menus/character.rpy:52
    old "[player.strength]\n[player.agility]\n[player.vitality]"
    new "[player.strength]\n[player.agility]\n[player.vitality]"

    # game/screens/menus/character.rpy:53
    old "\n{color=#FFD700}--- Mental Stats ---{/color}"
    new "\n{color=#FFD700}--- Estadísticas Mentales ---{/color}"

    # game/screens/menus/character.rpy:57
    old "{color=#B29EC1}Intelligence{/color} - coming soon.\n\n{color=#C6E2FF}Wisdom{/color} - every 10 point increase maximum spirituality by 1 point.\n\n{color=#FF958F}Charisma{/color} - no effect on combat. Used to make others agree with you during conversation.\n\nIncreased in the player room."
    new "{color=#B29EC1}Inteligencia{/color} - pronto.\n\n{color=#C6E2FF}Sabiduría{/color} - cada 10 puntos incrementa espiritualidad máxima por 1 punto.\n\n{color=#FF958F}nCarisma{/color} - sin efecto en combate. Usado para hacer a otros estar de acuerdo en conversación.\n\nIncrementado en habitación del jugador."

    # game/screens/menus/character.rpy:61
    old "Intelligence:\nWisdom:\nCharisma:"
    new "Inteligencia:\nSabiduría:\nCarisma:"

    # game/screens/menus/character.rpy:62
    old "[player.intelligence]\n[player.wisdom]\n[player.charisma]"
    new "[player.intelligence]\n[player.wisdom]\n[player.charisma]"

    # game/screens/menus/character.rpy:63
    old "\n{color=#FFD700}--- Other ---{/color}"
    new "\n{color=#FFD700}--- Otro ---{/color}"

    # game/screens/menus/character.rpy:67
    old "{color=#E4CA48}Luck{/color} - increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.\n\nCard draw - amount of cards you start your round with.\n\nMax hand - amount of cards you can hold simultaneously in combat."
    new "{color=#E4CA48}Suerte{/color} - aumenta la posibilidad de obtener buenas cartas, disminuye la posibilidad de encontrar oponentes fuertes. Incrementado con códigos de Discord o al negociar con ciertos seres.\n\nMano - cantidad de cartas con las que comienzas tu ronda.\n\nMáximo en mano - cantidad de cartas que puedes sostener simultáneamente en combate."

    # game/screens/menus/character.rpy:71
    old "Luck:\nCard draw:\nMax hand:"
    new "Suerte:\nMano:\nMáximo en mano:"

    # game/screens/menus/character.rpy:72
    old "[player.luck]\n[player.card_draw]\n[player.max_hand]"
    new "[player.luck]\n[player.card_draw]\n[player.max_hand]"
# TODO: Translation updated at 2022-01-25 22:41

translate spanish strings:

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"
    new "{b}{u}{color=#d26a6a}Salud{/color}{/u}{/b}\n{small}Daño que puedes recibir.{/small}\n\n{b}{u}{color=#C6E2FF}Espiritualidad{/color}{/u}{/b}\n{small}Consumida al usar cartas en combate. Recupera al comienzo de un nuevo turno.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"
    new "{b}{u}{color=#DAD1BF}Sanidad{/color}{/u}{/b}\n{small}Cuán capaz de razonamiento lógico eres. Llegar al 0% lleva al fin del juego.{/small}\n\n{b}{u}{color=#800080}Corrupción{/color}{/u}{/b}\n{small}Que tan degenerado estás. Alcanzar el 100% conduce al fin del juego.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"
    new "{b}{u}{color=#F4C25E}Fuerza{/color}{/u}{/b}\n{small}Aumenta el daño infligido en combate por 1 cada 5 puntos.{/small}\n\n{b}{u}{color=#32CD32}Agilidad{/color}{/u}{/b}\n{small}Cada punto da un 1% de evitar daño y aumenta la posibilidad de escapar del combate por 2%.{/small}\n\n{b}{u}{color=#A71930}Vitalidad{/color}{/u}{/b}\n{small}Cada punto aumenta tu salud máxima por 3.{/small}\n\n{small}Aumentada en gimnasio.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"
    new "{b}{u}{color=#B29EC1}Inteligencia{/color}{/b}{/u}\n{small}Usada en unos chequeos.{/small}\n\n{b}{u}{color=#C6E2FF}Sabiduría{/color}{/b}{/u}\n{small}Cada 10 puntos aumenta espiritualidad máxima por 1 punto.{/small}\n\n{b}{u}{color=#FF958F}Carisma{/color}{/b}{/u}\n{small}Se usa en muchos chequeos. Usada para que otros estén de acuerdo contigo en una conversación.{/small}\n\n{small}Aumentada en tu habitación.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"
    new "{b}{u}{color=#E4CA48}Suerte{/color}{/b}{/u}\n{small}Aumenta posibilidad de buenas cartas., disminuye la posibilidad de encontrarse con oponentes fuertes. Aumentada con códigos de Discord o comerciando con ciertos seres.{/small}"

    # game/screens/menus/character.rpy:45
    old "{gold}--- State ---{/gold}"
    new "{gold}--- Estado ---{/gold}"

    # game/screens/menus/character.rpy:53
    old "{color=#d26a6a}Health:{/color}"
    new "{color=#d26a6a}Salud:{/color}"

    # game/screens/menus/character.rpy:54
    old "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"
    new "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"

    # game/screens/menus/character.rpy:55
    old "\n{gold}--- Mental State ---{/gold}"
    new "\n{gold}--- Estado Mental ---{/gold}"

    # game/screens/menus/character.rpy:65
    old "\n{gold}--- Physical Stats ---{/gold}"
    new "\n{gold}--- Estadísticas Físicas ---{/gold}"

    # game/screens/menus/character.rpy:75
    old "\n{gold}--- Mental Stats ---{/gold}"
    new "\n{gold}--- Estadísticas Mentales ---{/gold}"

    # game/screens/menus/character.rpy:85
    old "\n{gold}--- Other ---{/gold}"
    new "\n{gold}--- Otro ---{/gold}"

    # game/screens/menus/character.rpy:93
    old "Luck:"
    new "Suerte:"

    # game/screens/menus/character.rpy:94
    old "[player.luck]"
    new "[player.luck]"

    # game/screens/menus/character.rpy:99
    old "\n{gold}--- Buffs ---{/gold}"
    new "\n{gold}--- Buffs ---{/gold}"
