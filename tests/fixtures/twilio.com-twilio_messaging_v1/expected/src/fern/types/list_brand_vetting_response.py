

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_brand_vetting_response_meta import ListBrandVettingResponseMeta
from .messaging_v1brand_registrations_brand_vetting import MessagingV1BrandRegistrationsBrandVetting


class ListBrandVettingResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[MessagingV1BrandRegistrationsBrandVetting]] = None
    meta: typing.Optional[ListBrandVettingResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
