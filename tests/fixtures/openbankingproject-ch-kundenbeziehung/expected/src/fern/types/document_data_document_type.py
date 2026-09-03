

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentDataDocumentType(enum.StrEnum):
    PASSPORT = "passport"
    ID_CARD = "id_card"
    DRIVING_LICENSE = "driving_license"
    EID = "eid"

    def visit(
        self,
        passport: typing.Callable[[], T_Result],
        id_card: typing.Callable[[], T_Result],
        driving_license: typing.Callable[[], T_Result],
        eid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentDataDocumentType.PASSPORT:
            return passport()
        if self is DocumentDataDocumentType.ID_CARD:
            return id_card()
        if self is DocumentDataDocumentType.DRIVING_LICENSE:
            return driving_license()
        if self is DocumentDataDocumentType.EID:
            return eid()
