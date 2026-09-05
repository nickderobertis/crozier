

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batched_facet_data_preprocessor_id_type import BatchedFacetDataPreprocessorIdType


class BatchedFacetDataPreprocessorId(UniversalBaseModel):
    type: BatchedFacetDataPreprocessorIdType
    id: str
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
