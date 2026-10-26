

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .coat import Coat
from .pot_outer_coat import PotOuterCoat


class Pot(UniversalBaseModel):
    potter: str
    outer_coat: typing_extensions.Annotated[
        PotOuterCoat,
        FieldMetadata(alias="outerCoat"),
        pydantic.Field(alias="outerCoat", description="The coat on the pot's outer wall."),
    ]
    """
    The coat on the pot's outer wall.
    """

    inner_coat: typing_extensions.Annotated[
        typing.Optional[Coat], FieldMetadata(alias="innerCoat"), pydantic.Field(alias="innerCoat")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
