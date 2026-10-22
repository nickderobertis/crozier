

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateTeamResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the team
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the team was created"),
    ] = None
    """
    The date and time the team was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the team was last updated"),
    ] = None
    """
    The date and time the team was last updated
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the team
    """

    organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="The ID of the organization"),
    ] = None
    """
    The ID of the organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
