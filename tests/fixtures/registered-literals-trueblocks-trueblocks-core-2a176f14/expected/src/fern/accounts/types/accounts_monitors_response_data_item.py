

import typing

from ...types.message import Message
from ...types.monitor import Monitor
from ...types.monitor_clean import MonitorClean

AccountsMonitorsResponseDataItem = typing.Union[Message, Monitor, MonitorClean]
