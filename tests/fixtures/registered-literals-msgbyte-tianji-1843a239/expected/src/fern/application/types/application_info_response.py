

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .application_info_response_application_store_infos_item import ApplicationInfoResponseApplicationStoreInfosItem


class ApplicationInfoResponse(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    deleted_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deletedAt"), pydantic.Field(alias="deletedAt")
    ] = None
    application_store_infos: typing_extensions.Annotated[
        typing.List[ApplicationInfoResponseApplicationStoreInfosItem],
        FieldMetadata(alias="applicationStoreInfos"),
        pydantic.Field(alias="applicationStoreInfos"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
