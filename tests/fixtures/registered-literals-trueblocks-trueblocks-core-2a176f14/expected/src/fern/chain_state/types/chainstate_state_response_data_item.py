

import typing

from ...types.function import Function
from ...types.message import Message
from ...types.parameter import Parameter
from ...types.result import Result
from ...types.state import State

ChainstateStateResponseDataItem = typing.Union[Function, Message, Parameter, Result, State]
