

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_end_customer_flowdown_status import PartnerEndCustomerFlowdownStatus
from .partner_end_customer_o_auth_institution import PartnerEndCustomerOAuthInstitution
from .partner_end_customer_questionnaire_status import PartnerEndCustomerQuestionnaireStatus
from .request_id import RequestId


class PartnerCustomerOAuthInstitutionsGetResponse(UniversalBaseModel):
    """
    Response schema for `/partner/customer/oauth_institutions/get`.
    """

    flowdown_status: typing.Optional[PartnerEndCustomerFlowdownStatus] = None
    institutions: typing.Optional[typing.List[PartnerEndCustomerOAuthInstitution]] = pydantic.Field(default=None)
    """
    The OAuth institutions with which the end customer's application is being registered.
    """

    questionnaire_status: typing.Optional[PartnerEndCustomerQuestionnaireStatus] = None
    request_id: typing.Optional[RequestId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
