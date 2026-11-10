

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .annotation_queue_item import AnnotationQueueItem
from .utils_meta_response import UtilsMetaResponse


class PaginatedAnnotationQueueItems(UniversalBaseModel):
    data: typing.List[AnnotationQueueItem]
    meta: UtilsMetaResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
