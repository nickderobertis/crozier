

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class WebsiteUpdateInfoResponse(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    domain: typing.Optional[str] = None
    share_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="shareId"), pydantic.Field(alias="shareId")
    ] = None
    reset_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resetAt"), pydantic.Field(alias="resetAt")
    ] = None
    monitor_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="monitorId"), pydantic.Field(alias="monitorId")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    deleted_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deletedAt"), pydantic.Field(alias="deletedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
