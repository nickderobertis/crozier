

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RegisterQueueResponseUserStatusValueReactionType(enum.StrEnum):
    """
    If present, a string indicating the type of emoji. Each emoji
    `reaction_type` has an independent namespace for values of `emoji_code`.

    Must be one of the following values:

    - `unicode_emoji` : In this namespace, `emoji_code` will be a
      dash-separated hex encoding of the sequence of Unicode codepoints
      that define this emoji in the Unicode specification.

    - `realm_emoji` : In this namespace, `emoji_code` will be the ID of
      the uploaded [custom emoji](/help/custom-emoji).

    - `zulip_extra_emoji` : These are special emoji included with Zulip.
      In this namespace, `emoji_code` will be the name of the emoji (e.g.
      "zulip").

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
        if self is RegisterQueueResponseUserStatusValueReactionType.UNICODE_EMOJI:
            return unicode_emoji()
        if self is RegisterQueueResponseUserStatusValueReactionType.REALM_EMOJI:
            return realm_emoji()
        if self is RegisterQueueResponseUserStatusValueReactionType.ZULIP_EXTRA_EMOJI:
            return zulip_extra_emoji()
