

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionRequestMessageContentPartImageImageUrlDetail(enum.StrEnum):
    """
    Specifies the detail level of the image. Learn more in the [Vision guide](/docs/guides/vision/low-or-high-fidelity-image-understanding).
    """

    AUTO = "auto"
    LOW = "low"
    HIGH = "high"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionRequestMessageContentPartImageImageUrlDetail.AUTO:
            return auto()
        if self is ChatCompletionRequestMessageContentPartImageImageUrlDetail.LOW:
            return low()
        if self is ChatCompletionRequestMessageContentPartImageImageUrlDetail.HIGH:
            return high()
