

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ComprehensiveCheckRequestCheckTypesItem(enum.StrEnum):
    SANCTIONS = "sanctions"
    PEP = "pep"
    CRIME = "crime"
    ADVERSE_MEDIA = "adverse_media"
    CREDIT = "credit"
    ZEK_IKO = "zek_iko"

    def visit(
        self,
        sanctions: typing.Callable[[], T_Result],
        pep: typing.Callable[[], T_Result],
        crime: typing.Callable[[], T_Result],
        adverse_media: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        zek_iko: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ComprehensiveCheckRequestCheckTypesItem.SANCTIONS:
            return sanctions()
        if self is ComprehensiveCheckRequestCheckTypesItem.PEP:
            return pep()
        if self is ComprehensiveCheckRequestCheckTypesItem.CRIME:
            return crime()
        if self is ComprehensiveCheckRequestCheckTypesItem.ADVERSE_MEDIA:
            return adverse_media()
        if self is ComprehensiveCheckRequestCheckTypesItem.CREDIT:
            return credit()
        if self is ComprehensiveCheckRequestCheckTypesItem.ZEK_IKO:
            return zek_iko()
