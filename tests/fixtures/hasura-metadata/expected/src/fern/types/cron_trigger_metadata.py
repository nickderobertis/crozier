

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cron_schedule import CronSchedule
from .cron_trigger_metadata_headers_item import CronTriggerMetadataHeadersItem
from .cron_trigger_metadata_request_transform import CronTriggerMetadataRequestTransform
from .cron_trigger_metadata_response_transform import CronTriggerMetadataResponseTransform
from .st_retry_conf import StRetryConf


class CronTriggerMetadata(UniversalBaseModel):
    comment: typing.Optional[str] = None
    headers: typing.Optional[typing.List[CronTriggerMetadataHeadersItem]] = None
    include_in_metadata: bool
    name: str
    payload: typing.Optional[typing.Dict[str, typing.Any]] = None
    request_transform: typing.Optional[CronTriggerMetadataRequestTransform] = None
    response_transform: typing.Optional[CronTriggerMetadataResponseTransform] = None
    retry_conf: typing.Optional[StRetryConf] = None
    schedule: CronSchedule
    webhook: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
