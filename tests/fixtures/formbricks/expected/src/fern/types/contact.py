

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Contact(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the contact
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="Optional external user identifier"),
    ] = None
    """
    Optional external user identifier
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the contact was created"),
    ]
    """
    When the contact was created
    """

    updated_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="When the contact was last updated"),
    ]
    """
    When the contact was last updated
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The Workspace this contact belongs to"),
    ]
    """
    The Workspace this contact belongs to
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
