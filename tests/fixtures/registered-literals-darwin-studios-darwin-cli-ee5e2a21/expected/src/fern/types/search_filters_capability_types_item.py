

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchFiltersCapabilityTypesItem(enum.StrEnum):
    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"
    CAPABILITY = "CAPABILITY"
    CAPACITY = "CAPACITY"
    ASSET = "ASSET"
    DATA = "DATA"
    RIGHT = "RIGHT"

    def visit(
        self,
        product: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
        capability: typing.Callable[[], T_Result],
        capacity: typing.Callable[[], T_Result],
        asset: typing.Callable[[], T_Result],
        data: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchFiltersCapabilityTypesItem.PRODUCT:
            return product()
        if self is SearchFiltersCapabilityTypesItem.SERVICE:
            return service()
        if self is SearchFiltersCapabilityTypesItem.CAPABILITY:
            return capability()
        if self is SearchFiltersCapabilityTypesItem.CAPACITY:
            return capacity()
        if self is SearchFiltersCapabilityTypesItem.ASSET:
            return asset()
        if self is SearchFiltersCapabilityTypesItem.DATA:
            return data()
        if self is SearchFiltersCapabilityTypesItem.RIGHT:
            return right()
