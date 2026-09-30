

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auto_trigger_log_cleanup_config import AutoTriggerLogCleanupConfig
from .citus_event_trigger_conf_event_trigger_conf_headers_item import CitusEventTriggerConfEventTriggerConfHeadersItem
from .citus_event_trigger_conf_event_trigger_conf_request_transform import (
    CitusEventTriggerConfEventTriggerConfRequestTransform,
)
from .citus_event_trigger_conf_event_trigger_conf_response_transform import (
    CitusEventTriggerConfEventTriggerConfResponseTransform,
)
from .citus_trigger_ops_def import CitusTriggerOpsDef
from .retry_conf import RetryConf


class CitusEventTriggerConfEventTriggerConf(UniversalBaseModel):
    cleanup_config: typing.Optional[AutoTriggerLogCleanupConfig] = None
    definition: CitusTriggerOpsDef
    headers: typing.Optional[typing.List[CitusEventTriggerConfEventTriggerConfHeadersItem]] = None
    name: str
    request_transform: typing.Optional[CitusEventTriggerConfEventTriggerConfRequestTransform] = None
    response_transform: typing.Optional[CitusEventTriggerConfEventTriggerConfResponseTransform] = None
    retry_conf: RetryConf
    trigger_on_replication: typing.Optional[bool] = None
    webhook: typing.Optional[str] = None
    webhook_from_env: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
