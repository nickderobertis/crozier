

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentSubmissionSharedBusinessEntitiesUserContentDefinition(UniversalBaseModel):
    """
    Relationship indicating that a User can manage submissions for the Content
    """

    content_definition_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ContentDefinitionID"),
        pydantic.Field(alias="ContentDefinitionID", description="The ID of the ContentDefinition."),
    ] = None
    """
    The ID of the ContentDefinition.
    """

    user_content_definition_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="UserContentDefinitionID"),
        pydantic.Field(
            alias="UserContentDefinitionID",
            description="Read Only. The ID of the User to ContentDefinition relationship.",
        ),
    ] = None
    """
    Read Only. The ID of the User to ContentDefinition relationship.
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="UserID"),
        pydantic.Field(alias="UserID", description="The ID of the user."),
    ] = None
    """
    The ID of the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
