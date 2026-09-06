

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batched_facet_data_facets_item import BatchedFacetDataFacetsItem
from .batched_facet_data_preprocessor import BatchedFacetDataPreprocessor
from .batched_facet_data_topic_maps_value_item import BatchedFacetDataTopicMapsValueItem
from .batched_facet_data_type import BatchedFacetDataType


class BatchedFacetData(UniversalBaseModel):
    type: BatchedFacetDataType
    preprocessor: typing.Optional[BatchedFacetDataPreprocessor] = pydantic.Field(default=None)
    """
    The preprocessor function to use for facet extraction. If not provided, the project default preprocessor will be used, falling back to the global 'thread' preprocessor.
    """

    facets: typing.List[BatchedFacetDataFacetsItem]
    topic_maps: typing.Optional[typing.Dict[str, typing.List[BatchedFacetDataTopicMapsValueItem]]] = pydantic.Field(
        default=None
    )
    """
    Topic maps that depend on facets in this batch, keyed by source facet name. Each source facet can have multiple topic maps.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
