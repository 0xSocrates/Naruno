#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import contextlib
import json
import os

from decentra_network.blockchain.block.block_main import Block
from decentra_network.config import TEMP_BLOCK_PATH
from decentra_network.lib.config_system import get_config
from decentra_network.lib.log import get_logger

logger = get_logger("BLOCKCHAIN")


def GetBlock(custom_TEMP_BLOCK_PATH=None):
    """
    Returns the block.
    """
    the_TEMP_BLOCK_PATH = (TEMP_BLOCK_PATH if custom_TEMP_BLOCK_PATH is None
                           else custom_TEMP_BLOCK_PATH)

    os.chdir(get_config()["main_folder"])

    highest_the_TEMP_BLOCK_PATH = the_TEMP_BLOCK_PATH
    highest_number = 0
    for file in os.listdir("db/"):
        if ("db/" + file).startswith(the_TEMP_BLOCK_PATH) and not ("db/" + file) == the_TEMP_BLOCK_PATH:           
            number = int(("db/" + file).replace(the_TEMP_BLOCK_PATH, ""))
            if number > highest_number:
                highest_number = number
                highest_the_TEMP_BLOCK_PATH = "db/" + file
            else:
                with contextlib.suppress(FileNotFoundError):
                    os.remove("db/" + file)




    with open(the_TEMP_BLOCK_PATH, "r") as block_file:
        the_block_json = json.load(block_file)
    result_normal = Block.load_json(the_block_json)

    with open(highest_the_TEMP_BLOCK_PATH, "r") as block_file:
        the_block_json = json.load(block_file)
    result_highest = Block.load_json(the_block_json)

    if result_normal.sequance_number + result_normal.empty_block_number > result_highest.sequance_number + result_highest.empty_block_number:
        return result_normal
    else:
        return result_highest


