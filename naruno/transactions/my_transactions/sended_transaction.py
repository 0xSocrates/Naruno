#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import json
import os

from distutils.log import info

from naruno.config import MY_TRANSACTION_PATH
from naruno.lib.config_system import get_config
from naruno.lib.notification import notification
from naruno.transactions.my_transactions.get_my_transaction import \
    GetMyTransaction
from naruno.transactions.my_transactions.save_my_transaction import \
    SaveMyTransaction
from naruno.transactions.transaction import Transaction


def SendedTransaction(tx: Transaction,
                      custom_currently_list: list = None) -> list:
    """
    Set sendedn the transaction.
    Parameters:
        tx: The transaction that is going to be validated.
    Returns:
        The list of the my transactions.
    """

    notification("Sended TX", f"{tx.data}:{tx.amount} to {tx.toUser}")

    custom_currently_list = (GetMyTransaction()
                             if custom_currently_list is None else
                             custom_currently_list)
    for i in custom_currently_list:
        if i[0].signature == tx.signature:
            i[2] = True
    SaveMyTransaction(custom_currently_list)
    return custom_currently_list
