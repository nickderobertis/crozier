

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_us_app_to_person_response_meta import ListUsAppToPersonResponseMeta
from .messaging_v1service_us_app_to_person import MessagingV1ServiceUsAppToPerson


class ListUsAppToPersonResponse(UniversalBaseModel):
    compliance: typing.Optional[typing.List[MessagingV1ServiceUsAppToPerson]] = None
    meta: typing.Optional[ListUsAppToPersonResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
