#
# Copyright (C) 2021-2022 by TeamSukun@Github, < https://github.com/TeamSukun >.
#
# This file is part of < https://github.com/TeamSukun/SukunXMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSukun/SukunXMusic/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
