

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_meta import ListMeta
from .page_metadata_entry import PageMetadataEntry


class PageMetadataListResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[PageMetadataEntry]] = None
    meta: typing.Optional[ListMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
