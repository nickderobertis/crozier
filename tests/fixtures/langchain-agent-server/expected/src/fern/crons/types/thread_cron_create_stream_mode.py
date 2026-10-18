

import typing

from .thread_cron_create_stream_mode_one import ThreadCronCreateStreamModeOne
from .thread_cron_create_stream_mode_zero_item import ThreadCronCreateStreamModeZeroItem

ThreadCronCreateStreamMode = typing.Union[
    typing.List[ThreadCronCreateStreamModeZeroItem], ThreadCronCreateStreamModeOne
]
