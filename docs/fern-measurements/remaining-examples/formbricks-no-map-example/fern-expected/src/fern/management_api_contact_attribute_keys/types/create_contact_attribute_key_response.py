

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_contact_attribute_key_response_type import CreateContactAttributeKeyResponseType


class CreateContactAttributeKeyResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the contact attribute key
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the contact attribute key was created"),
    ] = None
    """
    The date and time the contact attribute key was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the contact attribute key was last updated"),
    ] = None
    """
    The date and time the contact attribute key was last updated
    """

    is_unique: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isUnique"),
        pydantic.Field(alias="isUnique", description="Whether the attribute must have unique values across contacts"),
    ] = None
    """
    Whether the attribute must have unique values across contacts
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
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

    type: typing.Optional[CreateContactAttributeKeyResponseType] = pydantic.Field(default=None)
    """
    Whether this is a default or custom attribute
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The ID of the Workspace this attribute belongs to"),
    ] = None
    """
    The ID of the Workspace this attribute belongs to
    """

    environment_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="environmentId"),
        pydantic.Field(alias="environmentId", description="Deprecated alias for workspaceId."),
    ] = None
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
