

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteEventFeedbackDetail(enum.StrEnum):
    """
    Additionnal detail in case of success on some specific behavior :

    |Feature|Description|Behavior|
    |----------|:-------------|------:|
    |Lock Doors|Send a lock doors by force|NoCIDBlacklisted if lock is OK but IML not blacklisted, CIDBlacklisted is when the doors are locked and the IML is well blacklisted|
    """

    NO_CID_BLACKLISTED = "NoCIDBlacklisted"
    CID_BLACKLISTED = "CIDBlacklisted"

    def visit(
        self, no_cid_blacklisted: typing.Callable[[], T_Result], cid_blacklisted: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RemoteEventFeedbackDetail.NO_CID_BLACKLISTED:
            return no_cid_blacklisted()
        if self is RemoteEventFeedbackDetail.CID_BLACKLISTED:
            return cid_blacklisted()
