

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostV1VectorSearchRequestParams(UniversalBaseModel):
    """
    List of search parameters
    """

    radius: typing.Optional[float] = pydantic.Field(default=None)
    """
    The angle where the vector with the least similarity resides.
    """

    range_filter: float = pydantic.Field()
    """
    Used in combination to filter vector field values whose similarity to the query vector falls into a specific range.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
