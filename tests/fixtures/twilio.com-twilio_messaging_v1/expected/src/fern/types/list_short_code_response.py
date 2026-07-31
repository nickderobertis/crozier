

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_short_code_response_meta import ListShortCodeResponseMeta
from .messaging_v1service_short_code import MessagingV1ServiceShortCode


class ListShortCodeResponse(UniversalBaseModel):
    meta: typing.Optional[ListShortCodeResponseMeta] = None
    short_codes: typing.Optional[typing.List[MessagingV1ServiceShortCode]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
