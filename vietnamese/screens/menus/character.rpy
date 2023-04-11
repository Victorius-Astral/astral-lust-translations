# : Translation updated at 2021-12-24 07:09

translate vietnamese strings:

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#d26a6a}Health{/color}{/u}{/b}\n{small}How much damage you can take.{/small}\n\n{b}{u}{color=#C6E2FF}Spirituality{/color}{/u}{/b}\n{small}Consumed when using cards in combat. Recovers at the beginning of new turn.{/small}"
    new "{b}{u}{color=#d26a6a}Máu{/color}{/u}{/b}\n{small}Lượng sát thương mà bạn có thể chịu.{/small}\n\n{b}{u}{color=#C6E2FF}Tâm linh{/color}{/u}{/b}\n{small}Tiêu hao khi sử dụng thẻ trong chiến đấu. Hồi phục khi bắt đầu lượt mới.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#DAD1BF}Sanity{/color}{/u}{/b}\n{small}How capable of logical reasoning you are. Reaching 0% leads to game over.{/small}\n\n{b}{u}{color=#800080}Corruption{/color}{/u}{/b}\n{small}How degenerated you are. Reaching 100% leads to game over.{/small}"
    new "{b}{u}{color=#DAD1BF}Độ tỉnh táo{/color}{/u}{/b}\n{small}Khả năng suy luận logic của bạn. Đạt đến 0% dẫn đến trò chơi kết thúc.{/small}\n\n{b}{u}{color=#800080}Sự tha hóa{/color}{/u}{/b}\n{small}Bạn đã tha hóa đến mức nào. Đạt 100% dẫn đến trò chơi kết thúc.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#F4C25E}Strength{/color}{/u}{/b}\n{small}Increases damage dealt in combat by 1 every 5 points.{/small}\n\n{b}{u}{color=#32CD32}Agility{/color}{/u}{/b}\n{small}Every point gives 1% of avoiding damage and increases chance to escape combat by 2%.{/small}\n\n{b}{u}{color=#A71930}Vitality{/color}{/u}{/b}\n{small}Every point increases your maximum health by 3.{/small}\n\n{small}Increased at the gym.{/small}"
    new "{b}{u}{color=#F4C25E}Sức mạnh{/color}{/u}{/b}\n{small}Tăng sát thương gây ra trong chiến đấu lên 1 mỗi 5 điểm.{/small}\n\n{b}{u}{color=#32CD32}Nhanh nhẹn{/color}{/u}{/b}\n{small}Mỗi điểm cho 1% tránh được sát thương và tăng cơ hội thoát khỏi giao tranh lên 2%.{/small}\n\n{b}{u}{color=#A71930}Sinh lực{/color}{/u}{/b}\n{small}Mỗi điểm sẽ tăng máu tối đa của bạn lên 3.{/small}\n\n{small}Tăng lên khi tập trong phòng tâp.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#B29EC1}Intelligence{/color}{/b}{/u}\n{small}Used in some checks.{/small}\n\n{b}{u}{color=#C6E2FF}Wisdom{/color}{/b}{/u}\n{small}Every 10 point increase maximum spirituality by 1 point.{/small}\n\n{b}{u}{color=#FF958F}Charisma{/color}{/b}{/u}\n{small}Used in many checks. Used to make others agree with you during conversation.{/small}\n\n{small}Increased in the player room.{/small}"
    new "{b}{u}{color=#B29EC1}Trí tuệ{/color}{/b}{/u}\n{small}Khả năng suy luận của bạn.{/small}\n\n{b}{u}{color=#C6E2FF}Sự thông thái{/color}{/b}{/u}\n{small}Mỗi 10 điểm tăng tối đa 1 điểm tâm linh.{/small}\n\n{b}{u}{color=#FF958F}Sức thu hút{/color}{/b}{/u}\n{small}Được sử dụng để làm cho người khác đồng ý với bạn trong cuộc trò chuyện.{/small}\n\n{small}Tăng lên khi tập trong phòng người chơi.{/small}"

    # game/screens/menus/character.rpy:13
    old "{b}{u}{color=#E4CA48}Luck{/color}{/b}{/u}\n{small}Increases chance for good cards, decreases chance to meet strong opponents. Increased with codes from Discord or by trading with certain beings.{/small}"
    new "{b}{u}{color=#E4CA48}May mắn{/color}{/b}{/u}\n{small}Tăng cơ hội nhận được bài tốt, giảm cơ hội gặp đối thủ mạnh. Tăng với các mã từ Discord hoặc bằng cách giao dịch với một số thực thể nhất định.{/small}"

    # game/screens/menus/character.rpy:45
    old "State"
    new "Trạng thái"

    # game/screens/menus/character.rpy:53
    old "{color=#d26a6a}Health:{/color}"
    new "{color=#d26a6a}Máu:{/color}"

    # game/screens/menus/character.rpy:54
    old "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"
    new "{color=#d26a6a}[player.hp]/[player.hp_max]{/color}"

    # game/screens/menus/character.rpy:55
    old "Mental State"
    new "Trạng thái tinh thần"

    # game/screens/menus/character.rpy:63
    old "Sanity:\nCorruption:"
    new "Độ tỉnh táo:\nSự sa đọa:"

    # game/screens/menus/character.rpy:64
    old "[player.sanity]%\n[player.corruption]%"
    new "[player.sanity]%\n[player.corruption]%"

    # game/screens/menus/character.rpy:65
    old "Physical Stats"
    new "Chỉ số vật lý"

    # game/screens/menus/character.rpy:73
    old "Strength:\nAgility:\nVitality:"
    new "Sức mạnh:\nNhanh nhẹn:\nSinh lực:"

    # game/screens/menus/character.rpy:74
    old "[player.strength]\n[player.agility]\n[player.vitality]"
    new "[player.strength]\n[player.agility]\n[player.vitality]"

    # game/screens/menus/character.rpy:75
    old "Mental Stats"
    new "Chỉ số tinh thần"

    # game/screens/menus/character.rpy:83
    old "Intelligence:\nWisdom:\nCharisma:"
    new "Trí tuệ:\nSự thông thái:\nSức thu hút:"

    # game/screens/menus/character.rpy:84
    old "[player.intelligence]\n[player.wisdom]\n[player.charisma]"
    new "[player.intelligence]\n[player.wisdom]\n[player.charisma]"

    # game/screens/menus/character.rpy:85
    old "Other"
    new "Khác"

    # game/screens/menus/character.rpy:93
    old "Luck:"
    new "May mắn:"

    # game/screens/menus/character.rpy:94
    old "[player.luck]"
    new "[player.luck]"

    # game/screens/menus/character.rpy:99
    old "Buffs"
    new "Buffs"
