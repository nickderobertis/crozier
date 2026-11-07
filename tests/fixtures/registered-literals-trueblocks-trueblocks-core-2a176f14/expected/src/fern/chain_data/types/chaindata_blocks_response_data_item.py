

import typing

from ...types.appearance import Appearance
from ...types.block import Block
from ...types.block_count import BlockCount
from ...types.light_block import LightBlock
from ...types.log import Log
from ...types.message import Message
from ...types.trace import Trace
from ...types.trace_action import TraceAction
from ...types.trace_result import TraceResult
from ...types.withdrawal import Withdrawal

ChaindataBlocksResponseDataItem = typing.Union[
    Appearance, Block, BlockCount, LightBlock, Log, Message, Trace, TraceAction, TraceResult, Withdrawal
]
