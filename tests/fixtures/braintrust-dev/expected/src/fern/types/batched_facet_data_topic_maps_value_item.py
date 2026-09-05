

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .topic_map_data import TopicMapData


class BatchedFacetDataTopicMapsValueItem(UniversalBaseModel):
    function_name: str = pydantic.Field()
    """
    The name of the topic map function
    """

    topic_map_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the topic map function
    """

    topic_map_data: TopicMapData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
