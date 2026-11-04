

import typing

from ...types.function import Function
from ...types.log import Log
from ...types.message import Message
from ...types.parameter import Parameter

ChaindataLogsResponseDataItem = typing.Union[Function, Log, Message, Parameter]
