

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_text_data_debounce import MarimoTextDataDebounce
from .marimo_text_data_kind import MarimoTextDataKind


class MarimoTextData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    placeholder: str
    label: typing.Optional[str] = None
    kind: typing.Optional[MarimoTextDataKind] = None
    max_length: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxLength"), pydantic.Field(alias="maxLength")
    ] = None
    min_length: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minLength"), pydantic.Field(alias="minLength")
    ] = None
    full_width: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fullWidth"), pydantic.Field(alias="fullWidth")
    ] = None
    disabled: typing.Optional[bool] = None
    debounce: typing.Optional[MarimoTextDataDebounce] = None
    password_has_value: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="passwordHasValue"), pydantic.Field(alias="passwordHasValue")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
