

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedsSubscribeAgentResponseMergeStrategy(enum.StrEnum):
    UNIQUE_MESSAGES = "unique-messages"
    COMBINE_INTO_SINGLE_MESSAGE = "combine-into-single-message"

    def visit(
        self, unique_messages: typing.Callable[[], T_Result], combine_into_single_message: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FeedsSubscribeAgentResponseMergeStrategy.UNIQUE_MESSAGES:
            return unique_messages()
        if self is FeedsSubscribeAgentResponseMergeStrategy.COMBINE_INTO_SINGLE_MESSAGE:
            return combine_into_single_message()
