

import typing

from ...types.function import Function
from ...types.message import Message
from ...types.parameter import Parameter
from ...types.trace import Trace
from ...types.trace_action import TraceAction
from ...types.trace_count import TraceCount
from ...types.trace_filter import TraceFilter
from ...types.trace_result import TraceResult

ChaindataTracesResponseDataItem = typing.Union[
    Function, Message, Parameter, Trace, TraceAction, TraceCount, TraceFilter, TraceResult
]
