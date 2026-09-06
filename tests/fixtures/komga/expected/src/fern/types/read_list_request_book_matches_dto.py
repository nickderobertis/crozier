

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .read_list_request_book_dto import ReadListRequestBookDto
from .read_list_request_book_match_dto import ReadListRequestBookMatchDto


class ReadListRequestBookMatchesDto(UniversalBaseModel):
    matches: typing.List[ReadListRequestBookMatchDto]
    request: ReadListRequestBookDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
