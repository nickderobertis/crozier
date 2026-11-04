

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflow_retry_policy_webhook_on_retry import WorkflowRetryPolicyWebhookOnRetry
from .workflow_retry_rule import WorkflowRetryRule


class WorkflowRetryPolicy(UniversalBaseModel):
    max_retries: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of retries after the initial attempt
    """

    delay_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Fixed delay before the next attempt, in seconds
    """

    webhook_on_retry: typing.Optional[WorkflowRetryPolicyWebhookOnRetry] = pydantic.Field(default=None)
    """
    Whether to send a webhook for every attempt or only the final attempt
    """

    retry_on: typing.List[WorkflowRetryRule] = pydantic.Field()
    """
    Terminal status rules that enable retries
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
