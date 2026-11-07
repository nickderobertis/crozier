

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_mode_vector_vector import SearchModeVectorVector


class SearchModeVector(UniversalBaseModel):
    """
    Vector search mode: Search results are retrieved based on the similarity of query vectors with the indexed vectors.
    """

    vector: typing_extensions.Annotated[
        SearchModeVectorVector,
        FieldMetadata(alias="Vector"),
        pydantic.Field(
            alias="Vector",
            description="Vector search mode: Search results are retrieved based on the similarity of query vectors with the indexed vectors.",
        ),
    ]
    """
    Vector search mode: Search results are retrieved based on the similarity of query vectors with the indexed vectors.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
