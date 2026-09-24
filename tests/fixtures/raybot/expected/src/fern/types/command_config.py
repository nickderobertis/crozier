

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cargo_lift_config import CargoLiftConfig
from .cargo_lower_config import CargoLowerConfig


class CommandConfig(UniversalBaseModel):
    cargo_lift: typing_extensions.Annotated[
        CargoLiftConfig, FieldMetadata(alias="cargoLift"), pydantic.Field(alias="cargoLift")
    ]
    cargo_lower: typing_extensions.Annotated[
        CargoLowerConfig, FieldMetadata(alias="cargoLower"), pydantic.Field(alias="cargoLower")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
