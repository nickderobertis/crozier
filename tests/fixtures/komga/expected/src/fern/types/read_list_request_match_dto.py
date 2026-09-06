

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .read_list_match_dto import ReadListMatchDto
from .read_list_request_book_matches_dto import ReadListRequestBookMatchesDto


class ReadListRequestMatchDto(UniversalBaseModel):
    error_code: typing_extensions.Annotated[str, FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")]
    read_list_match: typing_extensions.Annotated[
        ReadListMatchDto, FieldMetadata(alias="readListMatch"), pydantic.Field(alias="readListMatch")
    ]
    requests: typing.List[ReadListRequestBookMatchesDto]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
