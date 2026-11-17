

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Embedding_Dense(UniversalBaseModel):
    """
    Embedding of a single input
    """

    vector_type: typing.Literal["dense"] = "dense"
    values: typing.List[float]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Embedding_Sparse(UniversalBaseModel):
    """
    Embedding of a single input
    """

    vector_type: typing.Literal["sparse"] = "sparse"
    sparse_values: typing.List[float]
    sparse_indices: typing.List[int]
    sparse_tokens: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Embedding = typing_extensions.Annotated[
    typing.Union[Embedding_Dense, Embedding_Sparse], pydantic.Field(discriminator="vector_type")
]
