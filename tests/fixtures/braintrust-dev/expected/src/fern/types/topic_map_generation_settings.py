

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .topic_map_generation_settings_algorithm import TopicMapGenerationSettingsAlgorithm
from .topic_map_generation_settings_dimension_reduction import TopicMapGenerationSettingsDimensionReduction


class TopicMapGenerationSettings(UniversalBaseModel):
    """
    Clustering and naming settings used to generate this topic map
    """

    algorithm: TopicMapGenerationSettingsAlgorithm
    dimension_reduction: TopicMapGenerationSettingsDimensionReduction
    sample_size: typing.Optional[int] = None
    n_clusters: typing.Optional[int] = None
    min_cluster_size: typing.Optional[int] = None
    min_samples: typing.Optional[int] = None
    hierarchy_threshold: typing.Optional[int] = None
    naming_model: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
