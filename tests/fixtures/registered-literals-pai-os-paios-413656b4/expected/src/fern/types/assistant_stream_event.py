

import typing

from .done_event import DoneEvent
from .error_event import ErrorEvent
from .message_stream_event import MessageStreamEvent
from .run_step_stream_event import RunStepStreamEvent
from .run_stream_event import RunStreamEvent
from .thread_stream_event import ThreadStreamEvent

AssistantStreamEvent = typing.Union[
    ThreadStreamEvent, RunStreamEvent, RunStepStreamEvent, MessageStreamEvent, ErrorEvent, DoneEvent
]
