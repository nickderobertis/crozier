

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetProjectScoreRequestScoreTypeOneItem(enum.StrEnum):
    """
    The type of the configured score
    """

    SLIDER = "slider"
    CATEGORICAL = "categorical"
    WEIGHTED = "weighted"
    MINIMUM = "minimum"
    MAXIMUM = "maximum"
    ONLINE = "online"
    FREE_FORM = "free-form"

    def visit(
        self,
        slider: typing.Callable[[], T_Result],
        categorical: typing.Callable[[], T_Result],
        weighted: typing.Callable[[], T_Result],
        minimum: typing.Callable[[], T_Result],
        maximum: typing.Callable[[], T_Result],
        online: typing.Callable[[], T_Result],
        free_form: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetProjectScoreRequestScoreTypeOneItem.SLIDER:
            return slider()
        if self is GetProjectScoreRequestScoreTypeOneItem.CATEGORICAL:
            return categorical()
        if self is GetProjectScoreRequestScoreTypeOneItem.WEIGHTED:
            return weighted()
        if self is GetProjectScoreRequestScoreTypeOneItem.MINIMUM:
            return minimum()
        if self is GetProjectScoreRequestScoreTypeOneItem.MAXIMUM:
            return maximum()
        if self is GetProjectScoreRequestScoreTypeOneItem.ONLINE:
            return online()
        if self is GetProjectScoreRequestScoreTypeOneItem.FREE_FORM:
            return free_form()
