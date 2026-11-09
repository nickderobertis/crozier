

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_end_customer_o_auth_institution_environments import PartnerEndCustomerOAuthInstitutionEnvironments


class PartnerEndCustomerOAuthInstitution(UniversalBaseModel):
    """
    The OAuth registration information for an institution.
    """

    classic_disablement_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which non-OAuth Item adds will no longer be supported for this institution, or an empty string if no such date has been set by the institution.
    """

    environments: typing.Optional[PartnerEndCustomerOAuthInstitutionEnvironments] = None
    institution_id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    production_enablement_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which the end customer's application was approved by the institution, or an empty string if their application has not yet been approved.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
