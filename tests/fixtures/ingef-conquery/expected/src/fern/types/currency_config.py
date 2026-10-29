

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CurrencyConfig(UniversalBaseModel):
    """
    Describes how the frontend shall interpret and display currency values.
    """

    prefix: typing.Optional[str] = None
    thousand_separator: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="thousandSeparator"), pydantic.Field(alias="thousandSeparator")
    ] = None
    decimal_separator: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="decimalSeparator"), pydantic.Field(alias="decimalSeparator")
    ] = None
    decimal_scale: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="decimalScale"), pydantic.Field(alias="decimalScale")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
