

import typing

from ...types.count import Count
from ...types.message import Message
from ...types.named_block import NamedBlock
from ...types.timestamp import Timestamp

ChaindataWhenResponseDataItem = typing.Union[Count, Message, NamedBlock, Timestamp]
