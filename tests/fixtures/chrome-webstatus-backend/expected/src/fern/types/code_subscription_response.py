

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_subscription_response_status import CodeSubscriptionResponseStatus
from .subscription_occurrence import SubscriptionOccurrence
from .subscription_trigger_writable import SubscriptionTriggerWritable


class CodeSubscriptionResponse(UniversalBaseModel):
    id: str
    vcs_provider: str
    vcs_installation_id: typing.Optional[str] = None
    vcs_repository_id: str
    repository_owner: str
    repository_name: str
    repository_full_name: str
    feature_id: typing.Optional[str] = None
    target_query: str
    triggers: typing.List[SubscriptionTriggerWritable]
    raw_directive: typing.Optional[str] = None
    occurrences: typing.List[SubscriptionOccurrence]
    occurrence_count: int
    status: CodeSubscriptionResponseStatus
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
