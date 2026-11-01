

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .glaze_or_swatch import GlazeOrSwatch
from .swatch_or_count import SwatchOrCount
from .swatch_or_name import SwatchOrName


class Finish(UniversalBaseModel):
    primary: typing.Optional[SwatchOrName] = None
    accent: typing.Optional[SwatchOrCount] = None
    coat: typing.Optional[GlazeOrSwatch] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
