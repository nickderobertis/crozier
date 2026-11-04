

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .page_get_all_pages_response_item_status_monitor_list_item import PageGetAllPagesResponseItemStatusMonitorListItem


class PageGetAllPagesResponseItem_Status(UniversalBaseModel):
    type: typing.Literal["status"] = "status"
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    slug: str
    title: str
    description: str
    body: typing.Dict[str, typing.Any]
    monitor_list: typing_extensions.Annotated[
        typing.List[PageGetAllPagesResponseItemStatusMonitorListItem],
        FieldMetadata(alias="monitorList"),
        pydantic.Field(alias="monitorList"),
    ]
    domain: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PageGetAllPagesResponseItem_Static(UniversalBaseModel):
    type: typing.Literal["static"] = "static"
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    slug: str
    title: str
    description: str
    domain: typing.Optional[str] = None
    payload: typing.Dict[str, typing.Any]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PageGetAllPagesResponseItem = typing_extensions.Annotated[
    typing.Union[PageGetAllPagesResponseItem_Status, PageGetAllPagesResponseItem_Static],
    pydantic.Field(discriminator="type"),
]
