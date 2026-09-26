

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoNumberData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ] = None
    label: typing.Optional[str] = None
    start: typing.Optional[float] = None
    stop: typing.Optional[float] = None
    step: typing.Optional[float] = None
    debounce: typing.Optional[bool] = None
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
