

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_end_customer_with_secrets import PartnerEndCustomerWithSecrets
from .request_id import RequestId


class PartnerCustomerCreateResponse(UniversalBaseModel):
    """
    Response schema for `/partner/customer/create`.
    """

    end_customer: typing.Optional[PartnerEndCustomerWithSecrets] = None
    request_id: typing.Optional[RequestId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
