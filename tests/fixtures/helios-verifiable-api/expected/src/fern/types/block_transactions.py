

import typing

from .hash32 import Hash32
from .transaction_info import TransactionInfo

BlockTransactions = typing.Union[typing.List[Hash32], typing.List[TransactionInfo]]
