

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_text_area_data_debounce import MarimoTextAreaDataDebounce


class MarimoTextAreaData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    placeholder: str
    label: typing.Optional[str] = None
    max_length: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxLength"), pydantic.Field(alias="maxLength")
    ] = None
    min_length: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minLength"), pydantic.Field(alias="minLength")
    ] = None
    disabled: typing.Optional[bool] = None
    debounce: typing.Optional[MarimoTextAreaDataDebounce] = None
    rows: typing.Optional[float] = None
    full_width: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fullWidth"), pydantic.Field(alias="fullWidth")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
