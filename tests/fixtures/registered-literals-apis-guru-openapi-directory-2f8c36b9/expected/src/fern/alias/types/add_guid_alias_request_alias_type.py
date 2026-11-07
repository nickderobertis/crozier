

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AddGuidAliasRequestAliasType(enum.StrEnum):
    GTIN = "gtin"
    ARTICLE = "article"
    MAPP = "mapp"
    ITEM = "item"
    RFID = "rfid"
    TRACKING = "tracking"
    ECLASS = "eclass"
    UNSPSC = "unspsc"
    PRODUCT = "product"
    MATERIAL = "material"
    REFERENCE = "reference"

    def visit(
        self,
        gtin: typing.Callable[[], T_Result],
        article: typing.Callable[[], T_Result],
        mapp: typing.Callable[[], T_Result],
        item: typing.Callable[[], T_Result],
        rfid: typing.Callable[[], T_Result],
        tracking: typing.Callable[[], T_Result],
        eclass: typing.Callable[[], T_Result],
        unspsc: typing.Callable[[], T_Result],
        product: typing.Callable[[], T_Result],
        material: typing.Callable[[], T_Result],
        reference: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddGuidAliasRequestAliasType.GTIN:
            return gtin()
        if self is AddGuidAliasRequestAliasType.ARTICLE:
            return article()
        if self is AddGuidAliasRequestAliasType.MAPP:
            return mapp()
        if self is AddGuidAliasRequestAliasType.ITEM:
            return item()
        if self is AddGuidAliasRequestAliasType.RFID:
            return rfid()
        if self is AddGuidAliasRequestAliasType.TRACKING:
            return tracking()
        if self is AddGuidAliasRequestAliasType.ECLASS:
            return eclass()
        if self is AddGuidAliasRequestAliasType.UNSPSC:
            return unspsc()
        if self is AddGuidAliasRequestAliasType.PRODUCT:
            return product()
        if self is AddGuidAliasRequestAliasType.MATERIAL:
            return material()
        if self is AddGuidAliasRequestAliasType.REFERENCE:
            return reference()
