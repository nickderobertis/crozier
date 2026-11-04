

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .audit_log_fetch_by_cursor_response_items_item_related_type import (
    AuditLogFetchByCursorResponseItemsItemRelatedType,
)


class AuditLogFetchByCursorResponseItemsItem(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    content: str
    related_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="relatedId"), pydantic.Field(alias="relatedId")
    ] = None
    related_type: typing_extensions.Annotated[
        typing.Optional[AuditLogFetchByCursorResponseItemsItemRelatedType],
        FieldMetadata(alias="relatedType"),
        pydantic.Field(alias="relatedType"),
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
