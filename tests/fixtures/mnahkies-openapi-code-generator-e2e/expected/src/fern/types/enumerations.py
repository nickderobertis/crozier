

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .enumerations_colors import EnumerationsColors


class Enumerations(UniversalBaseModel):
    colors: EnumerationsColors
    star_ratings: typing_extensions.Annotated[
        float, FieldMetadata(alias="starRatings"), pydantic.Field(alias="starRatings")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
