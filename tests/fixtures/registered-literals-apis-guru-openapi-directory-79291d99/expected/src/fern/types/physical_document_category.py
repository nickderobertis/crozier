

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PhysicalDocumentCategory(enum.StrEnum):
    """
    The type of identity document detected in the images provided. Will always be one of the following values:

      `drivers_license` - A driver's license for the associated country

      `id_card` - A general national identification card, distinct from driver's licenses

      `passport` - A passport for the associated country

      `residence_permit_card` - An identity document permitting a foreign citizen to <em>temporarily</em> reside in the associated country

      `resident_card` - An identity document permitting a foreign citizen to <em>permanently</em> reside in the associated country

    Note: This value may be different from the ID type that the user selects within Link. For example, if they select "Driver's License" but then submit a picture of a passport, this field will say `passport`
    """

    DRIVERS_LICENSE = "drivers_license"
    ID_CARD = "id_card"
    PASSPORT = "passport"
    RESIDENCE_PERMIT_CARD = "residence_permit_card"
    RESIDENT_CARD = "resident_card"

    def visit(
        self,
        drivers_license: typing.Callable[[], T_Result],
        id_card: typing.Callable[[], T_Result],
        passport: typing.Callable[[], T_Result],
        residence_permit_card: typing.Callable[[], T_Result],
        resident_card: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PhysicalDocumentCategory.DRIVERS_LICENSE:
            return drivers_license()
        if self is PhysicalDocumentCategory.ID_CARD:
            return id_card()
        if self is PhysicalDocumentCategory.PASSPORT:
            return passport()
        if self is PhysicalDocumentCategory.RESIDENCE_PERMIT_CARD:
            return residence_permit_card()
        if self is PhysicalDocumentCategory.RESIDENT_CARD:
            return resident_card()
