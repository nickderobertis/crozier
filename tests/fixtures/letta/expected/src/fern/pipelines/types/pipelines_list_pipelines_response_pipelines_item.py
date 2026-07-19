

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_list_pipelines_response_pipelines_item_config import PipelinesListPipelinesResponsePipelinesItemConfig
from .pipelines_list_pipelines_response_pipelines_item_integration_type import (
    PipelinesListPipelinesResponsePipelinesItemIntegrationType,
)


class PipelinesListPipelinesResponsePipelinesItem(UniversalBaseModel):
    id: str
    name: str
    organization_id: str
    project_id: str
    integration_id: str
    integration_type: PipelinesListPipelinesResponsePipelinesItemIntegrationType
    feed_id: str
    config: PipelinesListPipelinesResponsePipelinesItemConfig
    next_scheduled_at: typing.Optional[dt.datetime] = None
    last_run_at: typing.Optional[dt.datetime] = None
    disabled_at: typing.Optional[dt.datetime] = None
    created_at: dt.datetime
    updated_at: dt.datetime
    integration_display_name: typing.Optional[str] = None
    feed_name: typing.Optional[str] = None
    subscriber_count: typing.Optional[float] = None
    error_count: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
