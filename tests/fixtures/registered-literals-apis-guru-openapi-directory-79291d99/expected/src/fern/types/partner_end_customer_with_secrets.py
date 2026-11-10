

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .partner_end_customer import PartnerEndCustomer
from .partner_end_customer_secrets import PartnerEndCustomerSecrets


class PartnerEndCustomerWithSecrets(PartnerEndCustomer):
    """
    The details for the newly created end customer, including secrets for non-Production environments.
    """

    secrets: typing.Optional[PartnerEndCustomerSecrets] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
