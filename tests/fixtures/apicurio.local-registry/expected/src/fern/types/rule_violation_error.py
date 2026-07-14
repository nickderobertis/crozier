

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .error import Error
from .rule_violation_cause import RuleViolationCause


class RuleViolationError(Error):
    """
    All error responses, whether `4xx` or `5xx` will include one of these as the response
    body.
    """

    causes: typing.List[RuleViolationCause] = pydantic.Field()
    """
    List of rule violation causes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
