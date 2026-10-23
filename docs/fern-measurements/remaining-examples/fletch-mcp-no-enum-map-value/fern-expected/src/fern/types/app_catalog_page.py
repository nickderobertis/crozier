

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_catalog_page_items_item import AppCatalogPageItemsItem


class AppCatalogPage(UniversalBaseModel):
    source: str
    observed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="observedAt"), pydantic.Field(alias="observedAt")
    ] = None
    age_seconds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ageSeconds"), pydantic.Field(alias="ageSeconds")
    ] = None
    stale: bool
    error: typing.Optional[str] = None
    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    cadence_seconds: typing_extensions.Annotated[
        int, FieldMetadata(alias="cadenceSeconds"), pydantic.Field(alias="cadenceSeconds")
    ]
    note: str
    items: typing.List[AppCatalogPageItemsItem]
    total: int
    limit: int
    offset: int
    next_offset: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nextOffset"), pydantic.Field(alias="nextOffset")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
