

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auto_trigger_log_cleanup_config import AutoTriggerLogCleanupConfig
from .cockroach_event_trigger_conf_event_trigger_conf_headers_item import (
    CockroachEventTriggerConfEventTriggerConfHeadersItem,
)
from .cockroach_event_trigger_conf_event_trigger_conf_request_transform import (
    CockroachEventTriggerConfEventTriggerConfRequestTransform,
)
from .cockroach_event_trigger_conf_event_trigger_conf_response_transform import (
    CockroachEventTriggerConfEventTriggerConfResponseTransform,
)
from .cockroach_trigger_ops_def import CockroachTriggerOpsDef
from .retry_conf import RetryConf


class CockroachEventTriggerConfEventTriggerConf(UniversalBaseModel):
    cleanup_config: typing.Optional[AutoTriggerLogCleanupConfig] = None
    definition: CockroachTriggerOpsDef
    headers: typing.Optional[typing.List[CockroachEventTriggerConfEventTriggerConfHeadersItem]] = None
    name: str
    request_transform: typing.Optional[CockroachEventTriggerConfEventTriggerConfRequestTransform] = None
    response_transform: typing.Optional[CockroachEventTriggerConfEventTriggerConfResponseTransform] = None
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
