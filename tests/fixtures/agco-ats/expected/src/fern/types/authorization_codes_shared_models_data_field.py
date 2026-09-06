

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorization_codes_shared_models_data_field_type import AuthorizationCodesSharedModelsDataFieldType


class AuthorizationCodesSharedModelsDataField(UniversalBaseModel):
    digits_precision: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="DigitsPrecision"),
        pydantic.Field(
            alias="DigitsPrecision",
            description="The number of decimal digits to be used by this data field. Required only by the 'Float' data type. Must be in range 1 - 15.",
        ),
    ] = None
    """
    The number of decimal digits to be used by this data field. Required only by the 'Float' data type. Must be in range 1 - 15.
    """

    max_exponent: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MaxExponent"),
        pydantic.Field(
            alias="MaxExponent",
            description="The maximum exponent to be used by this data field. Required only by the 'Float' data type. May not be greater than 307.",
        ),
    ] = None
    """
    The maximum exponent to be used by this data field. Required only by the 'Float' data type. May not be greater than 307.
    """

    max_value: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="MaxValue"),
        pydantic.Field(
            alias="MaxValue",
            description="The maximum value that can be represented by this data field. Required only by the 'Decimal' data type.",
        ),
    ] = None
    """
    The maximum value that can be represented by this data field. Required only by the 'Decimal' data type.
    """

    min_exponent: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MinExponent"),
        pydantic.Field(
            alias="MinExponent",
            description="The minimum exponent to be used by this data field. Required only by the 'Float' data type. May not be less than -292.",
        ),
    ] = None
    """
    The minimum exponent to be used by this data field. Required only by the 'Float' data type. May not be less than -292.
    """

    min_value: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="MinValue"),
        pydantic.Field(
            alias="MinValue",
            description="The minimum value that can be represented by this data field. Required only by the 'Decimal' data type.",
        ),
    ] = None
    """
    The minimum value that can be represented by this data field. Required only by the 'Decimal' data type.
    """

    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The name of the field.")
    ]
    """
    The name of the field.
    """

    scale_factor: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="ScaleFactor"),
        pydantic.Field(
            alias="ScaleFactor",
            description="The resolution of values that can be represented by this data field. The base value is multiplied by this to compute the final value. Required only by the 'Decimal' data type.",
        ),
    ] = None
    """
    The resolution of values that can be represented by this data field. The base value is multiplied by this to compute the final value. Required only by the 'Decimal' data type.
    """

    signed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Signed"),
        pydantic.Field(
            alias="Signed",
            description="Indicates whether this value is signed. Required only by the 'Float' data type.",
        ),
    ] = None
    """
    Indicates whether this value is signed. Required only by the 'Float' data type.
    """

    type: typing_extensions.Annotated[
        AuthorizationCodesSharedModelsDataFieldType,
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The type of this data field."),
    ]
    """
    The type of this data field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
