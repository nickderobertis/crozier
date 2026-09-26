

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_datetime_data_precision import MarimoDatetimeDataPrecision


class MarimoDatetimeData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    label: typing.Optional[str] = None
    start: str
    stop: str
    step: typing.Optional[str] = None
    precision: typing.Optional[MarimoDatetimeDataPrecision] = None
    full_width: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fullWidth"), pydantic.Field(alias="fullWidth")
    ] = None
    disabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
