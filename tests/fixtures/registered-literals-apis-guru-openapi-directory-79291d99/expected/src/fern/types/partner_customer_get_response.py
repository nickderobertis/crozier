

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_end_customer import PartnerEndCustomer
from .request_id import RequestId


class PartnerCustomerGetResponse(UniversalBaseModel):
    """
    Response schema for `/partner/customer/get`.
    """

    end_customer: typing.Optional[PartnerEndCustomer] = None
    request_id: typing.Optional[RequestId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
