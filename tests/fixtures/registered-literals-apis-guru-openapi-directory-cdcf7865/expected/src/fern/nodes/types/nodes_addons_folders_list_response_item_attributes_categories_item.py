

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class NodesAddonsFoldersListResponseItemAttributesCategoriesItem(enum.StrEnum):
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
        if self is NodesAddonsFoldersListResponseItemAttributesCategoriesItem.DOCUMENTATION:
            return documentation()
        if self is NodesAddonsFoldersListResponseItemAttributesCategoriesItem.STORAGE:
            return storage()
        if self is NodesAddonsFoldersListResponseItemAttributesCategoriesItem.BIBLIOGRAPHY:
            return bibliography()
        if self is NodesAddonsFoldersListResponseItemAttributesCategoriesItem.OTHER:
            return other()
        if self is NodesAddonsFoldersListResponseItemAttributesCategoriesItem.SECURITY:
            return security()
        if self is NodesAddonsFoldersListResponseItemAttributesCategoriesItem.CITATIONS:
            return citations()
