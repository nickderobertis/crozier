

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpDataPersonJobTitleLevels(enum.StrEnum):
    """
    A person's current job title derived levels
    """

    UNPAID = "unpaid"
    TRAINING = "training"
    ENTRY = "entry"
    MANAGER = "manager"
    SENIOR = "senior"
    PARTNER = "partner"
    DIRECTOR = "director"
    VP = "vp"
    OWNER = "owner"
    CXO = "cxo"

    def visit(
        self,
        unpaid: typing.Callable[[], T_Result],
        training: typing.Callable[[], T_Result],
        entry: typing.Callable[[], T_Result],
        manager: typing.Callable[[], T_Result],
        senior: typing.Callable[[], T_Result],
        partner: typing.Callable[[], T_Result],
        director: typing.Callable[[], T_Result],
        vp: typing.Callable[[], T_Result],
        owner: typing.Callable[[], T_Result],
        cxo: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpDataPersonJobTitleLevels.UNPAID:
            return unpaid()
        if self is IpDataPersonJobTitleLevels.TRAINING:
            return training()
        if self is IpDataPersonJobTitleLevels.ENTRY:
            return entry()
        if self is IpDataPersonJobTitleLevels.MANAGER:
            return manager()
        if self is IpDataPersonJobTitleLevels.SENIOR:
            return senior()
        if self is IpDataPersonJobTitleLevels.PARTNER:
            return partner()
        if self is IpDataPersonJobTitleLevels.DIRECTOR:
            return director()
        if self is IpDataPersonJobTitleLevels.VP:
            return vp()
        if self is IpDataPersonJobTitleLevels.OWNER:
            return owner()
        if self is IpDataPersonJobTitleLevels.CXO:
            return cxo()
