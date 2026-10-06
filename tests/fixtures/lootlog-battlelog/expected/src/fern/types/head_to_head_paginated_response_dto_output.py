

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .head_to_head_paginated_response_dto_output_meta import HeadToHeadPaginatedResponseDtoOutputMeta
from .head_to_head_paginated_response_dto_output_pagination import HeadToHeadPaginatedResponseDtoOutputPagination
from .head_to_head_paginated_response_dto_output_records_item import HeadToHeadPaginatedResponseDtoOutputRecordsItem


class HeadToHeadPaginatedResponseDtoOutput(UniversalBaseModel):
    records: typing.List[HeadToHeadPaginatedResponseDtoOutputRecordsItem]
    pagination: HeadToHeadPaginatedResponseDtoOutputPagination
    meta: HeadToHeadPaginatedResponseDtoOutputMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
