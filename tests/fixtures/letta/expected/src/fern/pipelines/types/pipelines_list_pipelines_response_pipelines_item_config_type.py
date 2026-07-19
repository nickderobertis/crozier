

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelinesListPipelinesResponsePipelinesItemConfigType(enum.StrEnum):
    SLACK_CHANNEL_READER = "slack_channel_reader"

    def visit(self, slack_channel_reader: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelinesListPipelinesResponsePipelinesItemConfigType.SLACK_CHANNEL_READER:
            return slack_channel_reader()
