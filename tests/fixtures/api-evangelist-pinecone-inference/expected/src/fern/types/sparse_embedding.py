

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SparseEmbedding(UniversalBaseModel):
    """
    A sparse embedding of a single input
    """

    sparse_values: typing.List[float] = pydantic.Field()
    """
    The sparse embedding values.
    """

    sparse_indices: typing.List[int] = pydantic.Field()
    """
    The sparse embedding indices.
    """

    sparse_tokens: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The normalized tokens used to create the sparse embedding.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
