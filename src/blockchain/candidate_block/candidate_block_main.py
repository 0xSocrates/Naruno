#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


class candidate_block:
    def __init__(self,candidate_blocks=[], candidate_block_hashes=[]):

        self.candidate_blocks = candidate_blocks
        self.candidate_block_hashes = candidate_block_hashes