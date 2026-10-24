

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class MixBatchRequest_Recipe(UniversalBaseModel):
    """
    How the batch is sourced.
    """

    kind: typing.Literal["recipe"] = "recipe"
    recipe: str
    grams: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MixBatchRequest_Remix(UniversalBaseModel):
    """
    How the batch is sourced.
    """

    kind: typing.Literal["remix"] = "remix"
    batch_id: typing_extensions.Annotated[str, FieldMetadata(alias="batchId"), pydantic.Field(alias="batchId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MixBatchRequest = typing_extensions.Annotated[
    typing.Union[MixBatchRequest_Recipe, MixBatchRequest_Remix], pydantic.Field(discriminator="kind")
]
