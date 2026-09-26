

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_range_slider_data_orientation import MarimoRangeSliderDataOrientation


class MarimoRangeSliderData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        typing.List[float], FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    label: typing.Optional[str] = None
    start: float
    stop: float
    step: typing.Optional[float] = None
    steps: typing.Optional[typing.List[float]] = None
    debounce: typing.Optional[bool] = None
    orientation: typing.Optional[MarimoRangeSliderDataOrientation] = None
    show_value: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showValue"), pydantic.Field(alias="showValue")
    ] = None
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
