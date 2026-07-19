

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedsUpdateSubscriptionResponseMergeStrategy(enum.StrEnum):
    UNIQUE_MESSAGES = "unique-messages"
    COMBINE_INTO_SINGLE_MESSAGE = "combine-into-single-message"

    def visit(
        self, unique_messages: typing.Callable[[], T_Result], combine_into_single_message: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FeedsUpdateSubscriptionResponseMergeStrategy.UNIQUE_MESSAGES:
            return unique_messages()
        if self is FeedsUpdateSubscriptionResponseMergeStrategy.COMBINE_INTO_SINGLE_MESSAGE:
            return combine_into_single_message()
