

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_end_customer_status import PartnerEndCustomerStatus


class PartnerEndCustomer(UniversalBaseModel):
    """
    The details for an end customer.
    """

    client_id: typing.Optional[str] = None
    company_name: typing.Optional[str] = None
    status: typing.Optional[PartnerEndCustomerStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
