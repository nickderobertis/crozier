

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_data_eight_type import FunctionDataEightType
from .topic_map_generation_settings import TopicMapGenerationSettings


class FunctionDataEight(UniversalBaseModel):
    type: FunctionDataEightType
    source_facet: str = pydantic.Field()
    """
    The facet field name to use as input for classification
    """

    embedding_model: str = pydantic.Field()
    """
    The embedding model to use for embedding facet values
    """

    bundle_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Key of the topic map bundle in code_bundles bucket
    """

    report_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Key of the clustering report in code_bundles bucket
    """

    topic_names: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Mapping from topic_id to topic name
    """

    generation_settings: typing.Optional[TopicMapGenerationSettings] = None
    distance_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum distance to nearest centroid. If exceeded, returns no_match.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
