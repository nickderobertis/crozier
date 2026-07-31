

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_service_response_meta import ListServiceResponseMeta
from .messaging_v1service import MessagingV1Service


class ListServiceResponse(UniversalBaseModel):
    meta: typing.Optional[ListServiceResponseMeta] = None
    services: typing.Optional[typing.List[MessagingV1Service]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
