

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AddonsListResponseItemAttributesCategoriesItem(enum.StrEnum):
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
        if self is AddonsListResponseItemAttributesCategoriesItem.DOCUMENTATION:
            return documentation()
        if self is AddonsListResponseItemAttributesCategoriesItem.STORAGE:
            return storage()
        if self is AddonsListResponseItemAttributesCategoriesItem.BIBLIOGRAPHY:
            return bibliography()
        if self is AddonsListResponseItemAttributesCategoriesItem.OTHER:
            return other()
        if self is AddonsListResponseItemAttributesCategoriesItem.SECURITY:
            return security()
        if self is AddonsListResponseItemAttributesCategoriesItem.CITATIONS:
            return citations()
