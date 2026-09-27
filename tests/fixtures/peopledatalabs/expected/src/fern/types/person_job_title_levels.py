

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PersonJobTitleLevels(enum.StrEnum):
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
        if self is PersonJobTitleLevels.UNPAID:
            return unpaid()
        if self is PersonJobTitleLevels.TRAINING:
            return training()
        if self is PersonJobTitleLevels.ENTRY:
            return entry()
        if self is PersonJobTitleLevels.MANAGER:
            return manager()
        if self is PersonJobTitleLevels.SENIOR:
            return senior()
        if self is PersonJobTitleLevels.PARTNER:
            return partner()
        if self is PersonJobTitleLevels.DIRECTOR:
            return director()
        if self is PersonJobTitleLevels.VP:
            return vp()
        if self is PersonJobTitleLevels.OWNER:
            return owner()
        if self is PersonJobTitleLevels.CXO:
            return cxo()
