

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetGuidAliasTypesResponseItem(enum.StrEnum):
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
        if self is GetGuidAliasTypesResponseItem.GTIN:
            return gtin()
        if self is GetGuidAliasTypesResponseItem.ARTICLE:
            return article()
        if self is GetGuidAliasTypesResponseItem.MAPP:
            return mapp()
        if self is GetGuidAliasTypesResponseItem.ITEM:
            return item()
        if self is GetGuidAliasTypesResponseItem.RFID:
            return rfid()
        if self is GetGuidAliasTypesResponseItem.TRACKING:
            return tracking()
        if self is GetGuidAliasTypesResponseItem.ECLASS:
            return eclass()
        if self is GetGuidAliasTypesResponseItem.UNSPSC:
            return unspsc()
        if self is GetGuidAliasTypesResponseItem.PRODUCT:
            return product()
        if self is GetGuidAliasTypesResponseItem.MATERIAL:
            return material()
        if self is GetGuidAliasTypesResponseItem.REFERENCE:
            return reference()
