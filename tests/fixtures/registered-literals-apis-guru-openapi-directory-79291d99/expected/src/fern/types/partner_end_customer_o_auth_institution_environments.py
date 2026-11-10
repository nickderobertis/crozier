

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_end_customer_o_auth_institution_application_status import (
    PartnerEndCustomerOAuthInstitutionApplicationStatus,
)


class PartnerEndCustomerOAuthInstitutionEnvironments(UniversalBaseModel):
    """
    Registration statuses by environment.
    """

    development: typing.Optional[PartnerEndCustomerOAuthInstitutionApplicationStatus] = None
    production: typing.Optional[PartnerEndCustomerOAuthInstitutionApplicationStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
