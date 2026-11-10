

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .iso8601date_nullable import Iso8601DateNullable
from .risk_check_email_domain_is_custom import RiskCheckEmailDomainIsCustom
from .risk_check_email_domain_is_disposable import RiskCheckEmailDomainIsDisposable
from .risk_check_email_domain_is_free_provider import RiskCheckEmailDomainIsFreeProvider
from .risk_check_email_is_deliverable_status import RiskCheckEmailIsDeliverableStatus
from .risk_check_email_top_level_domain_is_suspicious import RiskCheckEmailTopLevelDomainIsSuspicious
from .risk_check_linked_service import RiskCheckLinkedService


class RiskCheckEmail(UniversalBaseModel):
    """
    Result summary object specifying values for `email` attributes of risk check.
    """

    breach_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Count of all known breaches of this email address if known.
    """

    domain_is_custom: RiskCheckEmailDomainIsCustom
    domain_is_disposable: RiskCheckEmailDomainIsDisposable
    domain_is_free_provider: RiskCheckEmailDomainIsFreeProvider
    domain_registered_at: typing.Optional[Iso8601DateNullable] = None
    first_breached_at: typing.Optional[Iso8601DateNullable] = None
    is_deliverable: RiskCheckEmailIsDeliverableStatus
    last_breached_at: typing.Optional[Iso8601DateNullable] = None
    linked_services: typing.List[RiskCheckLinkedService]
    top_level_domain_is_suspicious: RiskCheckEmailTopLevelDomainIsSuspicious

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
