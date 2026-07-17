

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Currency(UniversalBaseModel):
    """
    Currency
    """

    code: str = pydantic.Field()
    """
    Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format.
    """

    decimal_digits: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="decimalDigits"),
        pydantic.Field(alias="decimalDigits", description="Number of decimal digits."),
    ]
    """
    Number of decimal digits.
    """

    name: str = pydantic.Field()
    """
    Currency name.
    """

    name_plural: typing_extensions.Annotated[
        str, FieldMetadata(alias="namePlural"), pydantic.Field(alias="namePlural", description="Currency plural name")
    ]
    """
    Currency plural name
    """

    rounding: float = pydantic.Field()
    """
    Currency digit rounding.
    """

    symbol: str = pydantic.Field()
    """
    Currency symbol.
    """

    symbol_native: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="symbolNative"),
        pydantic.Field(alias="symbolNative", description="Currency native symbol."),
    ]
    """
    Currency native symbol.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
