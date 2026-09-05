

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .facet_data_preprocessor import FacetDataPreprocessor
from .facet_data_type import FacetDataType


class FacetData(UniversalBaseModel):
    type: FacetDataType
    preprocessor: typing.Optional[FacetDataPreprocessor] = pydantic.Field(default=None)
    """
    The preprocessor function to use for facet extraction. If not provided, the project default preprocessor will be used, falling back to the global 'thread' preprocessor.
    """

    prompt: str = pydantic.Field()
    """
    The prompt to use for LLM extraction. The preprocessed text will be provided as context.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model to use for facet extraction
    """

    embedding_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The embedding model to use for vectorizing facet results.
    """

    no_match_pattern: typing.Optional[str] = pydantic.Field(default=None)
    """
    Regex pattern to identify outputs that do not match the facet. If the output matches, the facet will be saved as 'no_match'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
