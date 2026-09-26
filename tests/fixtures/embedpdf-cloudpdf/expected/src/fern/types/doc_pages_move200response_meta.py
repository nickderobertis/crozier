

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_pages_move200response_meta_affected_pages_item import DocPagesMove200ResponseMetaAffectedPagesItem
from .doc_pages_move200response_meta_cache_delta import DocPagesMove200ResponseMetaCacheDelta


class DocPagesMove200ResponseMeta(UniversalBaseModel):
    affected_pages: typing_extensions.Annotated[
        typing.List[DocPagesMove200ResponseMetaAffectedPagesItem],
        FieldMetadata(alias="affectedPages"),
        pydantic.Field(alias="affectedPages"),
    ]
    cache_delta: typing_extensions.Annotated[
        typing.Optional[DocPagesMove200ResponseMetaCacheDelta],
        FieldMetadata(alias="cacheDelta"),
        pydantic.Field(alias="cacheDelta"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
