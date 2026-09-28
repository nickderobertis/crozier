

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .v2log_list_item import V2LogListItem


class V2LogListResponse(UniversalBaseModel):
    """
    A cursor-paginated page of workflow execution logs.
    """

    data: typing.List[V2LogListItem] = pydantic.Field()
    """
    Items in the current page.
    """

    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(
            alias="nextCursor",
            description="Opaque cursor for the next page. Send it back as `cursor`; `null` means there is nothing further to fetch. Never construct one yourself.",
        ),
    ] = None
    """
    Opaque cursor for the next page. Send it back as `cursor`; `null` means there is nothing further to fetch. Never construct one yourself.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(V2LogListResponse)
