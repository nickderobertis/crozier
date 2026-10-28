

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemCollectionType(enum.StrEnum):
    FEATURE_COLLECTION = "FeatureCollection"

    def visit(self, feature_collection: typing.Callable[[], T_Result]) -> T_Result:
        if self is ItemCollectionType.FEATURE_COLLECTION:
            return feature_collection()
