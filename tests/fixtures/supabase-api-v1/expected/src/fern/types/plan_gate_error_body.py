

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plan_gate_error_body_error import PlanGateErrorBodyError


class PlanGateErrorBody(UniversalBaseModel):
    message: str = pydantic.Field()
    """
    Human-readable explanation of the plan gate
    """

    error: typing.Optional[PlanGateErrorBodyError] = pydantic.Field(default=None)
    """
    Present on entitlement denials. Other errors with this status code (validation, billing state) carry only message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
