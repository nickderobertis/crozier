

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourceAttribute(enum.StrEnum):
    PROPERTIES = "Properties"
    METADATA = "Metadata"
    CREATION_POLICY = "CreationPolicy"
    UPDATE_POLICY = "UpdatePolicy"
    DELETION_POLICY = "DeletionPolicy"
    TAGS = "Tags"

    def visit(
        self,
        properties: typing.Callable[[], T_Result],
        metadata: typing.Callable[[], T_Result],
        creation_policy: typing.Callable[[], T_Result],
        update_policy: typing.Callable[[], T_Result],
        deletion_policy: typing.Callable[[], T_Result],
        tags: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceAttribute.PROPERTIES:
            return properties()
        if self is ResourceAttribute.METADATA:
            return metadata()
        if self is ResourceAttribute.CREATION_POLICY:
            return creation_policy()
        if self is ResourceAttribute.UPDATE_POLICY:
            return update_policy()
        if self is ResourceAttribute.DELETION_POLICY:
            return deletion_policy()
        if self is ResourceAttribute.TAGS:
            return tags()
