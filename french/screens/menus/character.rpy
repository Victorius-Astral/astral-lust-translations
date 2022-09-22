# : Translation updated at 2021-05-17 12:56

translate french strings:

    # game/screens/menus/character.rpy:27
    old "{color=#A71930}Health{/color} - how much damage you can take.\n\n{color=#C6E2FF}Spirituality{/color} - consumed when using cards in combat. Recovers at the beginning of new turn."
    new "{color=#A71930}Santé{/color} - combien de dégâts pouvez-vous recevoir.\n\n{color=#C6E2FF}Spiritualité{/color} - consommé lorsque les cartes sont utilisées en combat. Récupéré dans un nouveau quart de travail"

    # game/screens/menus/character.rpy:31
    old "{color=#A71930}Health:{/color}\n{color=#C6E2FF}Spirituality:{/color}"
    new "{color=#A71930}Santé:{/color}\n{color=#C6E2FF}Spiritualité:{/color}"

    # game/screens/menus/character.rpy:32
    old "{color=#A71930}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}"
    new "{color=#A71930}[player.hp]/[player.hp_max]{/color}\n{color=#C6E2FF}[player.spirit]/[player.spirit_max]{/color}"

    # game/screens/menus/character.rpy:33
    old "\n{color=#FFD700}--- Mental State ---{/color}"
    new "\n{color=#FFD700}--- État Mental ---{/color}"

    # game/screens/menus/character.rpy:37
    old "{color=#DAD1BF}Sanity{/color} - how capable of logical reasoning you are. Reaching 0% leads to game over.\n\n{color=#800080}Corruption{/color} - how degenerated you are. Reaching 100% leads to game over."
    new "{color=#DAD1BF}Santé Mentale{/color} - comme vous êtes capable de raisonnement logique. Atteindre 0 pour cent mène à la fin de la partie.\n\n{color=#800080}Corruption{/color} - comment tu es proche de la folie. Atteindre 100 pour 100 mène à la fin de la partie."

    # game/screens/menus/character.rpy:41
    old "Sanity:\nCorruption:"
    new "Santé Mentale:\nCorruption:"

    # game/screens/menus/character.rpy:42
    old "[player.sanity]%\n[player.corruption]%"
    new "[player.sanity]%\n[player.corruption]%"

    # game/screens/menus/character.rpy:43
    old "\n{color=#FFD700}--- Physical Stats ---{/color}"
    new "\n{color=#FFD700}--- Statistiques Physiques ---{/color}"

    # game/screens/menus/character.rpy:47
    old "{color=#F4C25E}Strength{/color} - increases damage dealt in combat by 1 every 5 points.\n\n{color=#32CD32}Agility{/color} - every point gives 1% of avoiding damage and increases chance to escape combat by 2%.\n\n{color=#A71930}Vitality{/color} - every point increases your maximum health by 3.\n\nIncreased at the gym."
    new "{color=#F4C25E}Force{/color} - augmente les dégâts de 1 tous les 5 points en combat.\n\n{color=#32CD32}Agilité{/color} - chaque point donne 1 pour 100 de dégâts d'évitement et augmente les possibilités d'évasion de 2 pour 100.\n\n{color=#A71930}Vitalité{/color} - chaque point augmente votre santé de 3.\n\nAugmenté dans la salle de gym."

    # game/screens/menus/character.rpy:51
    old "Strength:\nAgility:\nVitality:"
    new "Force:\nAgilité:\nVitalité:"

    # game/screens/menus/character.rpy:52
    old "[player.strength]\n[player.agility]\n[player.vitality]"
    new "[player.strength]\n[player.agility]\n[player.vitality]"

    # game/screens/menus/character.rpy:53
    old "\n{color=#FFD700}--- Mental Stats ---{/color}"
    new "\n{color=#FFD700}--- Statistiques Mentales ---{/color}"

    # game/screens/menus/character.rpy:57
    old "{color=#B29EC1}Intelligence{/color} - coming soon.\n\n{color=#C6E2FF}Wisdom{/color} - every 10 point increase maximum spirituality by 1 point.\n\n{color=#FF958F}Charisma{/color} - no effect on combat. Used to make others agree with you during conversation.\n\nIncreased in the player room."
    new "{color=#B29EC1}Intelligence{/color} - bientôt.\n\n{color=#C6E2FF}Sagesse{/color} - chaque 10 points augmente la spiritualité maximale de 1 point.\n\n{color=#FF958F}Charisme{/color} - aucun effet au combat. Utilisé pour mettre les autres d'accord dans la conversation.\n\nAugmenté dans la chambre du joueur."

    # game/screens/menus/character.rpy:61
    old "Intelligence:\nWisdom:\nCharisma:"
    new "Intelligence:\nSagesse:\nCharisme:"

    # game/screens/menus/character.rpy:62
    old "[player.intelligence]\n[player.wisdom]\n[player.charisma]"
    new "[player.intelligence]\n[player.wisdom]\n[player.charisma]"

    # game/screens/menus/character.rpy:63
    old "\n{color=#FFD700}--- Other ---{/color}"
    new "\n{color=#FFD700}--- Autre ---{/color}"

    # game/screens/menus/character.rpy:67
    old "{color=#E4CA48}Luck{/color} - increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.\n\nCard draw - amount of cards you start your round with.\n\nMax hand - amount of cards you can hold simultaneously in combat."
    new "{color=#E4CA48}Chance{/color} - cela augmente les chances d'obtenir de bonnes cartes, diminue les chances de rencontrer des adversaires forts. Augmenté avec les codes de Discorde ou lors de négociations avec certains êtres.\n\nMain - le nombre de cartes avec lesquelles vous commencez votre tour.\n\nMaximum en nombre de main de cartes que vous pouvez détenir simultanément en combat."

    # game/screens/menus/character.rpy:71
    old "Luck:\nCard draw:\nMax hand:"
    new "Chance:\nMain:\nMain maximum:"

    # game/screens/menus/character.rpy:72
    old "[player.luck]\n[player.card_draw]\n[player.max_hand]"
    new "[player.luck]\n[player.card_draw]\n[player.max_hand]"
# : Translation updated at 2022-01-25 22:41

translate french strings:

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"
    new "{b}{u}{color=#d26a6a}Santé{/color}{/u}{/b}\n{small}Dommages que vous pouvez recevoir.{/small}\n\n{b}{u}{color=#C6E2FF}Spiritualité{/color}{/u}{/b}\n{small}Consommé lors de l'utilisation de cartes au combat. Récupère au début d'un nouveau quart de travail.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"
    new "{b}{u}{color=#DAD1BF}Santé{/color}{/u}{/b}\n{small}À quel point êtes-vous capable de raisonnement logique. Atteindre 0 pour 100 mène à la fin de la partie.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}Comment tu es fou. Atteindre 100 pour 100 mène à la fin de la partie.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"
    new "{b}{u}{color=#F4C25E}Force{/color}{/u}{/b}\n{small}Augmente les dégâts infligés au combat de 1 tous les 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agilité{/color}{/u}{/b}\n{small}Chaque point donne 1 pour 100 pour éviter les dégâts et augmente les chances d'échapper au combat de 2 pour 100.{/small}\n\n{b}{u}{color=#A71930}Vitalité{/color}{/u}{/b}\n{small}Chaque point augmente votre santé maximale de 3.{/small}\n\n{small}Augmenté dans la salle de gym.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"
    new "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Utilisé dans quelques contrôles.{/small}\n\n{b}{u}{color=#C6E2FF}Sagesse{/color}{/b}{/u}\n{small}Tous les 10 points augmente la spiritualité maximale de 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisme{/color}{/b}{/u}\n{small}Il est utilisé dans de nombreux contrôles. Utilisé pour amener les autres à être d'accord avec vous dans une conversation.{/small}\n\n{small}Augmenté dans votre chambre.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"
    new "{b}{u}{color=#E4CA48}Chance{/color}{/b}{/u}\n{small}Augmente les chances de bonnes cartes., diminue les chances de rencontrer des adversaires puissants. Jouer avec des codes Discord ou échanger avec certains êtres.{/small}"

    # game/screens/menus/character.rpy:45
    old "State"
    new "État"

    # game/screens/menus/character.rpy:53
    old "{color=#d26a6a}Health:{/color}"
    new "{color=#d26a6a}Santé:{/color}"

    # game/screens/menus/character.rpy:54
    old "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"
    new "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"

    # game/screens/menus/character.rpy:55
    old "Mental State"
    new "État Mental"

    # game/screens/menus/character.rpy:65
    old "Physical Stats"
    new "Statistiques Physiques"

    # game/screens/menus/character.rpy:75
    old "Mental Stats"
    new "Statistiques Mentales"

    # game/screens/menus/character.rpy:85
    old "Other"
    new "Autre"

    # game/screens/menus/character.rpy:93
    old "Luck:"
    new "Chance:"

    # game/screens/menus/character.rpy:94
    old "[player.luck]"
    new "[player.luck]"

    # game/screens/menus/character.rpy:99
    old "Buffs"
    new "Buffles"
