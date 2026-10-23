

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class CreateContactResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    workspace_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ] = None
    environment_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="environmentId"),
        pydantic.Field(alias="environmentId", description="Deprecated alias for workspaceId."),
    ] = None
    """
    Deprecated alias for workspaceId.
    """

    attributes: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
