

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchByAliasRequestAliasType(enum.StrEnum):
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
        if self is SearchByAliasRequestAliasType.GTIN:
            return gtin()
        if self is SearchByAliasRequestAliasType.ARTICLE:
            return article()
        if self is SearchByAliasRequestAliasType.MAPP:
            return mapp()
        if self is SearchByAliasRequestAliasType.ITEM:
            return item()
        if self is SearchByAliasRequestAliasType.RFID:
            return rfid()
        if self is SearchByAliasRequestAliasType.TRACKING:
            return tracking()
        if self is SearchByAliasRequestAliasType.ECLASS:
            return eclass()
        if self is SearchByAliasRequestAliasType.UNSPSC:
            return unspsc()
        if self is SearchByAliasRequestAliasType.PRODUCT:
            return product()
        if self is SearchByAliasRequestAliasType.MATERIAL:
            return material()
        if self is SearchByAliasRequestAliasType.REFERENCE:
            return reference()
