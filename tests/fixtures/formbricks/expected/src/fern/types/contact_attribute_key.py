

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_attribute_key_type import ContactAttributeKeyType


class ContactAttributeKey(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the contact attribute key
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the contact attribute key was created"),
    ]
    """
    The date and time the contact attribute key was created
    """

    updated_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the contact attribute key was last updated"),
    ]
    """
    The date and time the contact attribute key was last updated
    """

    is_unique: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isUnique"),
        pydantic.Field(alias="isUnique", description="Whether the attribute must have unique values across contacts"),
    ]
    """
    Whether the attribute must have unique values across contacts
    """

    key: str = pydantic.Field()
    """
    The attribute identifier used in the system
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name for the attribute
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the attribute
    """

    type: ContactAttributeKeyType = pydantic.Field()
    """
    Whether this is a default or custom attribute
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The ID of the Workspace this attribute belongs to"),
    ]
    """
    The ID of the Workspace this attribute belongs to
    """

    environment_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="environmentId"),
        pydantic.Field(alias="environmentId", description="Deprecated alias for workspaceId."),
    ]
    """
    Deprecated alias for workspaceId.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
