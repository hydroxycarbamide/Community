#!/usr/bin/python3

# Change the look of Adwaita, with ease
# Copyright (C) 2024 Hydroxycarbamide
# Copyright (C) 2022 Gradience Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Created by @dominichayesferen for Gradience Team

import os
import json
from colorama import Fore, Style

directories = [
    "curated",
    "official"
]

original_variables = [
    "headerbar_bg_color",
    "headerbar_fg_color",
    "headerbar_backdrop_color",
    "headerbar_shade_color"
]

destination_variables = [
    "sidebar_bg_color",
    "sidebar_fg_color",
    "sidebar_backdrop_color",
    "sidebar_shade_color"
]

for directory in directories:
    for i in os.listdir(directory):
        file_path = directory + "/" + i
        # print(i)
        with open(file_path, 'r') as pa:
            # NOTE: There is no .json filter in the above code
            # be aware that if any non-json file were to be added to that folder,
            # json.loads will likely raise an exception
            palette = json.loads(pa.read())

        if not "variables" in palette:
            print(f"{Fore.RED}\"variables\" not in {i}{Style.RESET_ALL}")
            continue

        for original_variable, destination_variable in zip(original_variables, destination_variables):
            if not original_variable in palette["variables"]:
                print(f"{Fore.RED}\"{original_variable}\" not in {i}{Style.RESET_ALL}")
                continue

            palette["variables"][destination_variable] = palette["variables"][original_variable]

        
        with open(file_path, 'w') as pa:
            json.dump(palette, pa, indent=4)
