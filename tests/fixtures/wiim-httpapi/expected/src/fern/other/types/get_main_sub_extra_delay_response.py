

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_main_sub_extra_delay_response_body import GetMainSubExtraDelayResponseBody


class GetMainSubExtraDelayResponse(UniversalBaseModel):
    category: typing.Optional[str] = None
    body: typing.Optional[GetMainSubExtraDelayResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
