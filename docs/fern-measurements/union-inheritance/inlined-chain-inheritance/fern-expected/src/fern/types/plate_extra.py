

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .plate_extra_plate_type import PlateExtraPlateType


class PlateExtra(UniversalBaseModel):
    plate_type: typing_extensions.Annotated[
        typing.Optional[PlateExtraPlateType], FieldMetadata(alias="plateType"), pydantic.Field(alias="plateType")
    ] = None
    serial: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
