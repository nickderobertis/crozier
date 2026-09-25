

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews(enum.StrEnum):
    """
    Controls how animated images should be played in the message feed in the web/desktop application.

    - "always" - Always play the animated images in the message feed.
    - "on_hover" - Play the animated images on hover over them in the message feed.
    - "never" - Never play animated images in the message feed.

    **Changes**: New in Zulip 9.0 (feature level 275). Previously, animated images
    always used to play in the message feed by default. This setting controls this
    behaviour.
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
        if self is UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews.ALWAYS:
            return always()
        if self is UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews.ON_HOVER:
            return on_hover()
        if self is UpdateRealmUserSettingsDefaultsRequestWebAnimateImagePreviews.NEVER:
            return never()
