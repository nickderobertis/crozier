

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .raw_parse_result_output_format import RawParseResultOutputFormat
from .raw_parse_result_profile import RawParseResultProfile


class RawParseResult(UniversalBaseModel):
    output_format: RawParseResultOutputFormat
    provider: str
    model: str
    profile: RawParseResultProfile
    result: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
