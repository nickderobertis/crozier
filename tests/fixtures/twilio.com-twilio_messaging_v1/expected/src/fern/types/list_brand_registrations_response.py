

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_brand_registrations_response_meta import ListBrandRegistrationsResponseMeta
from .messaging_v1brand_registrations import MessagingV1BrandRegistrations


class ListBrandRegistrationsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[MessagingV1BrandRegistrations]] = None
    meta: typing.Optional[ListBrandRegistrationsResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
