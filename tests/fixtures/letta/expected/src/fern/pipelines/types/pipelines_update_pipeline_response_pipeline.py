

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_update_pipeline_response_pipeline_config import PipelinesUpdatePipelineResponsePipelineConfig
from .pipelines_update_pipeline_response_pipeline_integration_type import (
    PipelinesUpdatePipelineResponsePipelineIntegrationType,
)


class PipelinesUpdatePipelineResponsePipeline(UniversalBaseModel):
    id: str
    name: str
    organization_id: str
    project_id: str
    integration_id: str
    integration_type: PipelinesUpdatePipelineResponsePipelineIntegrationType
    feed_id: str
    config: PipelinesUpdatePipelineResponsePipelineConfig
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
