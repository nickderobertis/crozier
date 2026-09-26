

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemAwayReactionType(enum.StrEnum):
    """
    The [emoji type](/api/update-status#parameter-reaction_type) for
    the emoji the user selected for their new status.

    This will be `""` for users who set a status without selecting
    an emoji.

    **Changes**: New in Zulip 5.0 (feature level 86).
    """

    UNICODE_EMOJI = "unicode_emoji"
    REALM_EMOJI = "realm_emoji"
    ZULIP_EXTRA_EMOJI = "zulip_extra_emoji"

    def visit(
        self,
        unicode_emoji: typing.Callable[[], T_Result],
        realm_emoji: typing.Callable[[], T_Result],
        zulip_extra_emoji: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetEventsResponseEventsItemAwayReactionType.UNICODE_EMOJI:
            return unicode_emoji()
        if self is GetEventsResponseEventsItemAwayReactionType.REALM_EMOJI:
            return realm_emoji()
        if self is GetEventsResponseEventsItemAwayReactionType.ZULIP_EXTRA_EMOJI:
            return zulip_extra_emoji()
