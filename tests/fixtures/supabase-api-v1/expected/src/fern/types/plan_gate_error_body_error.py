

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plan_gate_error_body_error_code import PlanGateErrorBodyErrorCode


class PlanGateErrorBodyError(UniversalBaseModel):
    """
    Present on entitlement denials. Other errors with this status code (validation, billing state) carry only message.
    """

    code: PlanGateErrorBodyErrorCode = pydantic.Field()
    """
    Machine-readable marker for plan-gated denials
    """

    feature: str = pydantic.Field()
    """
    Entitlement feature key that failed the check
    """

    upgrade_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Billing page URL for the organization, present when the org is resolvable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
