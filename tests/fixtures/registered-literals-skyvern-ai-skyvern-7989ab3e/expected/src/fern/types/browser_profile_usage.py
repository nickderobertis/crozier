

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .browser_profile_usage_credential import BrowserProfileUsageCredential
from .browser_profile_usage_workflow import BrowserProfileUsageWorkflow


class BrowserProfileUsage(UniversalBaseModel):
    workflows: typing.Optional[typing.List[BrowserProfileUsageWorkflow]] = None
    credentials: typing.Optional[typing.List[BrowserProfileUsageCredential]] = None
    recent_seeded_run_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
