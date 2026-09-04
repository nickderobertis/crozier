

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CollectionBelongsToType(enum.StrEnum):
    """
    Indicates whether a collection belongs to a component release or a product release
    """

    COMPONENT_RELEASE = "COMPONENT_RELEASE"
    PRODUCT_RELEASE = "PRODUCT_RELEASE"

    def visit(
        self, component_release: typing.Callable[[], T_Result], product_release: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CollectionBelongsToType.COMPONENT_RELEASE:
            return component_release()
        if self is CollectionBelongsToType.PRODUCT_RELEASE:
            return product_release()
