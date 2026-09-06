

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_project_automation_config_btql_export_credentials import CreateProjectAutomationConfigBtqlExportCredentials
from .create_project_automation_config_btql_export_export_definition import (
    CreateProjectAutomationConfigBtqlExportExportDefinition,
)
from .create_project_automation_config_btql_export_format import CreateProjectAutomationConfigBtqlExportFormat
from .create_project_automation_config_environment_update_action import (
    CreateProjectAutomationConfigEnvironmentUpdateAction,
)
from .create_project_automation_config_logs_action import CreateProjectAutomationConfigLogsAction
from .retention_object_type import RetentionObjectType
from .topic_automation_config_backfill_time_range import TopicAutomationConfigBackfillTimeRange
from .topic_automation_config_facet_functions_item import TopicAutomationConfigFacetFunctionsItem
from .topic_automation_config_scope import TopicAutomationConfigScope
from .topic_automation_data_scope import TopicAutomationDataScope
from .topic_map_function_automation import TopicMapFunctionAutomation


class CreateProjectAutomationConfig_Logs(UniversalBaseModel):
    """
    The configuration for the automation rule
    """

    event_type: typing.Literal["logs"] = "logs"
    btql_filter: str
    interval_seconds: float
    action: CreateProjectAutomationConfigLogsAction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateProjectAutomationConfig_BtqlExport(UniversalBaseModel):
    """
    The configuration for the automation rule
    """

    event_type: typing.Literal["btql_export"] = "btql_export"
    export_definition: CreateProjectAutomationConfigBtqlExportExportDefinition
    export_path: str
    format: CreateProjectAutomationConfigBtqlExportFormat
    interval_seconds: float
    credentials: CreateProjectAutomationConfigBtqlExportCredentials
    batch_size: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateProjectAutomationConfig_Retention(UniversalBaseModel):
    """
    The configuration for the automation rule
    """

    event_type: typing.Literal["retention"] = "retention"
    object_type: RetentionObjectType
    retention_days: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateProjectAutomationConfig_EnvironmentUpdate(UniversalBaseModel):
    """
    The configuration for the automation rule
    """

    event_type: typing.Literal["environment_update"] = "environment_update"
    environment_filter: typing.Optional[typing.List[str]] = None
    action: CreateProjectAutomationConfigEnvironmentUpdateAction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateProjectAutomationConfig_Topic(UniversalBaseModel):
    """
    The configuration for the automation rule
    """

    event_type: typing.Literal["topic"] = "topic"
    sampling_rate: float
    facet_functions: typing.List[TopicAutomationConfigFacetFunctionsItem]
    topic_map_functions: typing.List[TopicMapFunctionAutomation]
    scope: typing.Optional[TopicAutomationConfigScope] = None
    data_scope: typing.Optional[TopicAutomationDataScope] = None
    btql_filter: typing.Optional[str] = None
    rerun_seconds: typing.Optional[float] = None
    relabel_overlap_seconds: typing.Optional[float] = None
    backfill_time_range: typing.Optional[TopicAutomationConfigBackfillTimeRange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateProjectAutomationConfig = typing_extensions.Annotated[
    typing.Union[
        CreateProjectAutomationConfig_Logs,
        CreateProjectAutomationConfig_BtqlExport,
        CreateProjectAutomationConfig_Retention,
        CreateProjectAutomationConfig_EnvironmentUpdate,
        CreateProjectAutomationConfig_Topic,
    ],
    pydantic.Field(discriminator="event_type"),
]
