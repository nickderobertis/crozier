

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSettingsRequestWebAnimateImagePreviews(enum.StrEnum):
    """
    Controls how animated images should be played in the message feed in the web/desktop application.

    - "always" - Always play the animated images in the message feed.
    - "on_hover" - Play the animated images on hover over them in the message feed.
    - "never" - Never play animated images in the message feed.

    **Changes**: New in Zulip 9.0 (feature level 275).
    """

    ALWAYS = "always"
    ON_HOVER = "on_hover"
    NEVER = "never"

    def visit(
        self,
        always: typing.Callable[[], T_Result],
        on_hover: typing.Callable[[], T_Result],
        never: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateSettingsRequestWebAnimateImagePreviews.ALWAYS:
            return always()
        if self is UpdateSettingsRequestWebAnimateImagePreviews.ON_HOVER:
            return on_hover()
        if self is UpdateSettingsRequestWebAnimateImagePreviews.NEVER:
            return never()
