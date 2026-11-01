

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .barge_hull import BargeHull


class Barge(UniversalBaseModel):
    """
    A towed vessel.
    """

    hull: typing.Optional[BargeHull] = None
    cargo_tonnes: typing_extensions.Annotated[
        float, FieldMetadata(alias="cargoTonnes"), pydantic.Field(alias="cargoTonnes")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
