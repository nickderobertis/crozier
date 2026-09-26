

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_manifest200response_pages_item_cache import DocManifest200ResponsePagesItemCache
from .doc_manifest200response_pages_item_state import DocManifest200ResponsePagesItemState


class DocManifest200ResponsePagesItem(UniversalBaseModel):
    state: DocManifest200ResponsePagesItemState
    cache: DocManifest200ResponsePagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
