

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BackgroundChecksRequestCheckTypesItem(enum.StrEnum):
    SANCTIONS = "sanctions"
    PEP = "pep"
    ADVERSE_MEDIA = "adverse_media"
    IDENTITY_VERIFICATION = "identity_verification"
    SANCTIONS_UPDATE = "sanctions_update"
    PEP_UPDATE = "pep_update"

    def visit(
        self,
        sanctions: typing.Callable[[], T_Result],
        pep: typing.Callable[[], T_Result],
        adverse_media: typing.Callable[[], T_Result],
        identity_verification: typing.Callable[[], T_Result],
        sanctions_update: typing.Callable[[], T_Result],
        pep_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BackgroundChecksRequestCheckTypesItem.SANCTIONS:
            return sanctions()
        if self is BackgroundChecksRequestCheckTypesItem.PEP:
            return pep()
        if self is BackgroundChecksRequestCheckTypesItem.ADVERSE_MEDIA:
            return adverse_media()
        if self is BackgroundChecksRequestCheckTypesItem.IDENTITY_VERIFICATION:
            return identity_verification()
        if self is BackgroundChecksRequestCheckTypesItem.SANCTIONS_UPDATE:
            return sanctions_update()
        if self is BackgroundChecksRequestCheckTypesItem.PEP_UPDATE:
            return pep_update()
