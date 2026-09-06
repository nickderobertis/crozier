

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageRenderingMode(enum.StrEnum):
    """
    Controls how images are rendered in the UI: 'auto' loads images automatically, 'click_to_load' shows a placeholder until clicked, 'blocked' prevents image loading entirely
    """

    AUTO = "auto"
    CLICK_TO_LOAD = "click_to_load"
    BLOCKED = "blocked"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        click_to_load: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImageRenderingMode.AUTO:
            return auto()
        if self is ImageRenderingMode.CLICK_TO_LOAD:
            return click_to_load()
        if self is ImageRenderingMode.BLOCKED:
            return blocked()
