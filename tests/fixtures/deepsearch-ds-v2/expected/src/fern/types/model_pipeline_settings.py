

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_pipeline_settings_clusters_item import ModelPipelineSettingsClustersItem
from .model_pipeline_settings_normalization_item import ModelPipelineSettingsNormalizationItem
from .model_pipeline_settings_page_item import ModelPipelineSettingsPageItem
from .model_pipeline_settings_tables_item import ModelPipelineSettingsTablesItem


class ModelPipelineSettings(UniversalBaseModel):
    clusters: typing.List[ModelPipelineSettingsClustersItem]
    page: typing.List[ModelPipelineSettingsPageItem]
    tables: typing.List[ModelPipelineSettingsTablesItem]
    normalization: typing.List[ModelPipelineSettingsNormalizationItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
