

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ToolboxSetsItem_Chisel(UniversalBaseModel):
    kind: typing.Literal["chisel"] = "chisel"
    width_mm: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="widthMm"), pydantic.Field(alias="widthMm")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ToolboxSetsItem_Plane(UniversalBaseModel):
    kind: typing.Literal["plane"] = "plane"
    sole_mm: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="soleMm"), pydantic.Field(alias="soleMm")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ToolboxSetsItem = typing_extensions.Annotated[
    typing.Union[ToolboxSetsItem_Chisel, ToolboxSetsItem_Plane], pydantic.Field(discriminator="kind")
]
