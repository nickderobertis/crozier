

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContentSubmissionListPolicy(enum.StrEnum):
    OFF = "off"
    CONTRIBUTORS = "contributors"
    EVERYONE = "everyone"

    def visit(
        self,
        off: typing.Callable[[], T_Result],
        contributors: typing.Callable[[], T_Result],
        everyone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContentSubmissionListPolicy.OFF:
            return off()
        if self is ContentSubmissionListPolicy.CONTRIBUTORS:
            return contributors()
        if self is ContentSubmissionListPolicy.EVERYONE:
            return everyone()
