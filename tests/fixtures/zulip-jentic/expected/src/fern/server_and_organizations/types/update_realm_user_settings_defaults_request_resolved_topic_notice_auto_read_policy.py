

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy(enum.StrEnum):
    """
    Controls whether the resolved-topic notices are marked as read.

    - "always" - Always mark resolved-topic notices as read.
    - "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
    - "never" - Never mark resolved-topic notices as read.

    **Changes**: New in Zulip 11.0 (feature level 385).
    """

    ALWAYS = "always"
    EXCEPT_FOLLOWED = "except_followed"
    NEVER = "never"

    def visit(
        self,
        always: typing.Callable[[], T_Result],
        except_followed: typing.Callable[[], T_Result],
        never: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy.ALWAYS:
            return always()
        if self is UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy.EXCEPT_FOLLOWED:
            return except_followed()
        if self is UpdateRealmUserSettingsDefaultsRequestResolvedTopicNoticeAutoReadPolicy.NEVER:
            return never()
