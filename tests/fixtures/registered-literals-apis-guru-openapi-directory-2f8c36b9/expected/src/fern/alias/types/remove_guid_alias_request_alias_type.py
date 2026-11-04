

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RemoveGuidAliasRequestAliasType(enum.StrEnum):
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
        if self is RemoveGuidAliasRequestAliasType.GTIN:
            return gtin()
        if self is RemoveGuidAliasRequestAliasType.ARTICLE:
            return article()
        if self is RemoveGuidAliasRequestAliasType.MAPP:
            return mapp()
        if self is RemoveGuidAliasRequestAliasType.ITEM:
            return item()
        if self is RemoveGuidAliasRequestAliasType.RFID:
            return rfid()
        if self is RemoveGuidAliasRequestAliasType.TRACKING:
            return tracking()
        if self is RemoveGuidAliasRequestAliasType.ECLASS:
            return eclass()
        if self is RemoveGuidAliasRequestAliasType.UNSPSC:
            return unspsc()
        if self is RemoveGuidAliasRequestAliasType.PRODUCT:
            return product()
        if self is RemoveGuidAliasRequestAliasType.MATERIAL:
            return material()
        if self is RemoveGuidAliasRequestAliasType.REFERENCE:
            return reference()
