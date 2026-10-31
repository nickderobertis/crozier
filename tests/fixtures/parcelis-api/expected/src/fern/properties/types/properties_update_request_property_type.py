

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PropertiesUpdateRequestPropertyType(enum.StrEnum):
    APARTMENT = "Apartment"
    COMMERCIAL = "Commercial"
    CONDO = "Condo"
    DUPLEX = "Duplex"
    HOA = "HOA"
    HOUSE = "House"
    MIXED_USE = "Mixed-Use"
    OTHER = "Other"
    PARKING = "Parking"
    SELF_STORAGE = "Self-storage"
    MANUFACTURED_HOME = "Manufactured Home"
    TRAILER = "Trailer"

    def visit(
        self,
        apartment: typing.Callable[[], T_Result],
        commercial: typing.Callable[[], T_Result],
        condo: typing.Callable[[], T_Result],
        duplex: typing.Callable[[], T_Result],
        hoa: typing.Callable[[], T_Result],
        house: typing.Callable[[], T_Result],
        mixed_use: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        parking: typing.Callable[[], T_Result],
        self_storage: typing.Callable[[], T_Result],
        manufactured_home: typing.Callable[[], T_Result],
        trailer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PropertiesUpdateRequestPropertyType.APARTMENT:
            return apartment()
        if self is PropertiesUpdateRequestPropertyType.COMMERCIAL:
            return commercial()
        if self is PropertiesUpdateRequestPropertyType.CONDO:
            return condo()
        if self is PropertiesUpdateRequestPropertyType.DUPLEX:
            return duplex()
        if self is PropertiesUpdateRequestPropertyType.HOA:
            return hoa()
        if self is PropertiesUpdateRequestPropertyType.HOUSE:
            return house()
        if self is PropertiesUpdateRequestPropertyType.MIXED_USE:
            return mixed_use()
        if self is PropertiesUpdateRequestPropertyType.OTHER:
            return other()
        if self is PropertiesUpdateRequestPropertyType.PARKING:
            return parking()
        if self is PropertiesUpdateRequestPropertyType.SELF_STORAGE:
            return self_storage()
        if self is PropertiesUpdateRequestPropertyType.MANUFACTURED_HOME:
            return manufactured_home()
        if self is PropertiesUpdateRequestPropertyType.TRAILER:
            return trailer()
