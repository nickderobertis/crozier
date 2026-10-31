

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parse_request_output_format import ParseRequestOutputFormat


class ParseRequest(UniversalBaseModel):
    ocr_model: str
    ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = None
    file_id: typing.Optional[str] = None
    output_format: typing.Optional[ParseRequestOutputFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
