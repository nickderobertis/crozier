

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_alpha_sender_response_meta import ListAlphaSenderResponseMeta
from .messaging_v1service_alpha_sender import MessagingV1ServiceAlphaSender


class ListAlphaSenderResponse(UniversalBaseModel):
    alpha_senders: typing.Optional[typing.List[MessagingV1ServiceAlphaSender]] = None
    meta: typing.Optional[ListAlphaSenderResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
