

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntityDocumentType(enum.StrEnum):
    """
    The kind of official document represented by this object.

    `bik` - Russian bank code

    `business_number` - A number that uniquely identifies the business within a category of businesses

    `imo` - Number assigned to the entity by the International Maritime Organization

    `other` - Any document not covered by other categories

    `swift` - Number identifying a bank and branch.

    `tax_id` - Identification issued for the purpose of collecting taxes
    """

    BIK = "bik"
    BUSINESS_NUMBER = "business_number"
    IMO = "imo"
    OTHER = "other"
    SWIFT = "swift"
    TAX_ID = "tax_id"

    def visit(
        self,
        bik: typing.Callable[[], T_Result],
        business_number: typing.Callable[[], T_Result],
        imo: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        swift: typing.Callable[[], T_Result],
        tax_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntityDocumentType.BIK:
            return bik()
        if self is EntityDocumentType.BUSINESS_NUMBER:
            return business_number()
        if self is EntityDocumentType.IMO:
            return imo()
        if self is EntityDocumentType.OTHER:
            return other()
        if self is EntityDocumentType.SWIFT:
            return swift()
        if self is EntityDocumentType.TAX_ID:
            return tax_id()
