

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RecastOrder_Bell(UniversalBaseModel):
    kind: typing.Literal["bell"] = "bell"
    weight_kg: typing_extensions.Annotated[float, FieldMetadata(alias="weightKg"), pydantic.Field(alias="weightKg")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RecastOrder_Handbell(UniversalBaseModel):
    kind: typing.Literal["handbell"] = "handbell"
    octaves: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RecastOrder = typing_extensions.Annotated[
    typing.Union[RecastOrder_Bell, RecastOrder_Handbell], pydantic.Field(discriminator="kind")
]
