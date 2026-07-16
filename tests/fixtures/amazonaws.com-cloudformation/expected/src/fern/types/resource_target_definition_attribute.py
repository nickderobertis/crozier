

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResourceTargetDefinitionAttribute(str, enum.Enum):
    """
    Indicates which resource attribute is triggering this update, such as a change in the resource attribute's <code>Metadata</code>, <code>Properties</code>, or <code>Tags</code>.
    """

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
        if self is ResourceTargetDefinitionAttribute.PROPERTIES:
            return properties()
        if self is ResourceTargetDefinitionAttribute.METADATA:
            return metadata()
        if self is ResourceTargetDefinitionAttribute.CREATION_POLICY:
            return creation_policy()
        if self is ResourceTargetDefinitionAttribute.UPDATE_POLICY:
            return update_policy()
        if self is ResourceTargetDefinitionAttribute.DELETION_POLICY:
            return deletion_policy()
        if self is ResourceTargetDefinitionAttribute.TAGS:
            return tags()
