

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesAddonsListResponseItemAttributesCategoriesItem(enum.StrEnum):
    DOCUMENTATION = "documentation"
    STORAGE = "storage"
    BIBLIOGRAPHY = "bibliography"
    OTHER = "other"
    SECURITY = "security"
    CITATIONS = "citations"

    def visit(
        self,
        documentation: typing.Callable[[], T_Result],
        storage: typing.Callable[[], T_Result],
        bibliography: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
        citations: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NodesAddonsListResponseItemAttributesCategoriesItem.DOCUMENTATION:
            return documentation()
        if self is NodesAddonsListResponseItemAttributesCategoriesItem.STORAGE:
            return storage()
        if self is NodesAddonsListResponseItemAttributesCategoriesItem.BIBLIOGRAPHY:
            return bibliography()
        if self is NodesAddonsListResponseItemAttributesCategoriesItem.OTHER:
            return other()
        if self is NodesAddonsListResponseItemAttributesCategoriesItem.SECURITY:
            return security()
        if self is NodesAddonsListResponseItemAttributesCategoriesItem.CITATIONS:
            return citations()
