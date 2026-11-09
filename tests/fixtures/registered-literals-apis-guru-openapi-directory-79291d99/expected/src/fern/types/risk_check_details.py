

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identity_verification_step_status import IdentityVerificationStepStatus
from .risk_check_behavior import RiskCheckBehavior
from .risk_check_device import RiskCheckDevice
from .risk_check_email import RiskCheckEmail
from .risk_check_phone import RiskCheckPhone


class RiskCheckDetails(UniversalBaseModel):
    """
    Additional information for the `risk_check` step.
    """

    behavior: typing.Optional[RiskCheckBehavior] = None
    devices: typing.List[RiskCheckDevice] = pydantic.Field()
    """
    Array of result summary objects specifying values for `device` attributes of risk check.
    """

    email: typing.Optional[RiskCheckEmail] = None
    phone: typing.Optional[RiskCheckPhone] = None
    status: IdentityVerificationStepStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
