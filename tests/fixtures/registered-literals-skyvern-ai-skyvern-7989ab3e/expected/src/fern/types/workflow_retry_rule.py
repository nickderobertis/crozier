

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflow_retry_rule_status import WorkflowRetryRuleStatus


class WorkflowRetryRule(UniversalBaseModel):
    status: WorkflowRetryRuleStatus = pydantic.Field()
    """
    Terminal status that triggers a retry rule; canceled is accepted for forward compatibility, but a canceled run never retries in the current runtime, including explicit API/UI cancels.
    """

    error_codes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional error codes. The rule matches when any listed code is present.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
