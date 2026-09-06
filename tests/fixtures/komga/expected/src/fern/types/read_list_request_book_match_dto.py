

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .read_list_request_book_match_book_dto import ReadListRequestBookMatchBookDto
from .read_list_request_book_match_series_dto import ReadListRequestBookMatchSeriesDto


class ReadListRequestBookMatchDto(UniversalBaseModel):
    books: typing.List[ReadListRequestBookMatchBookDto]
    series: ReadListRequestBookMatchSeriesDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
