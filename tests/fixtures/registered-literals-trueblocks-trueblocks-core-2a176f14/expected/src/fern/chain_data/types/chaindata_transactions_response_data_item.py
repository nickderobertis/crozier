

import typing

from ...types.appearance import Appearance
from ...types.function import Function
from ...types.log import Log
from ...types.message import Message
from ...types.parameter import Parameter
from ...types.transaction import Transaction

ChaindataTransactionsResponseDataItem = typing.Union[Appearance, Function, Log, Message, Parameter, Transaction]
