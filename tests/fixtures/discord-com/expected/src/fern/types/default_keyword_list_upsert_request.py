

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .automod_event_type import AutomodEventType
from .default_keyword_list_trigger_metadata import DefaultKeywordListTriggerMetadata
from .default_keyword_list_upsert_request_actions_item import DefaultKeywordListUpsertRequestActionsItem
from .snowflake_type import SnowflakeType


class DefaultKeywordListUpsertRequest(UniversalBaseModel):
    name: str
    event_type: AutomodEventType
    actions: typing.Optional[typing.List[DefaultKeywordListUpsertRequestActionsItem]] = None
    enabled: typing.Optional[bool] = None
    exempt_roles: typing.Optional[typing.List[SnowflakeType]] = None
    exempt_channels: typing.Optional[typing.List[SnowflakeType]] = None
    trigger_type: int
    trigger_metadata: DefaultKeywordListTriggerMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
