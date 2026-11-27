

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BeadRef_Glass(UniversalBaseModel):
    bead_type: typing_extensions.Annotated[
        typing.Literal["GLASS"], FieldMetadata(alias="beadType"), pydantic.Field(alias="beadType")
    ] = "GLASS"
    glass_id: typing_extensions.Annotated[str, FieldMetadata(alias="glassId"), pydantic.Field(alias="glassId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BeadRef_Wood(UniversalBaseModel):
    bead_type: typing_extensions.Annotated[
        typing.Literal["WOOD"], FieldMetadata(alias="beadType"), pydantic.Field(alias="beadType")
    ] = "WOOD"
    wood_id: typing_extensions.Annotated[str, FieldMetadata(alias="woodId"), pydantic.Field(alias="woodId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


BeadRef = typing_extensions.Annotated[
    typing.Union[BeadRef_Glass, BeadRef_Wood], pydantic.Field(discriminator="bead_type")
]
