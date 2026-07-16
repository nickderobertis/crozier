

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ObError1(UniversalBaseModel):
    error_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ErrorCode"),
        pydantic.Field(alias="ErrorCode", description="Low level textual error code, e.g., UK.OBIE.Field.Missing"),
    ]
    """
    Low level textual error code, e.g., UK.OBIE.Field.Missing
    """

    message: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Message"),
        pydantic.Field(
            alias="Message",
            description="A description of the error that occurred. e.g., 'A mandatory field isn't supplied' or 'RequestedExecutionDateTime must be in future'\nOBIE doesn't standardise this field",
        ),
    ]
    """
    A description of the error that occurred. e.g., 'A mandatory field isn't supplied' or 'RequestedExecutionDateTime must be in future'
    OBIE doesn't standardise this field
    """

    path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Path"),
        pydantic.Field(
            alias="Path",
            description="Recommended but optional reference to the JSON Path of the field with error, e.g., Data.Initiation.InstructedAmount.Currency",
        ),
    ] = None
    """
    Recommended but optional reference to the JSON Path of the field with error, e.g., Data.Initiation.InstructedAmount.Currency
    """

    url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Url"),
        pydantic.Field(
            alias="Url",
            description="URL to help remediate the problem, or provide more information, or to API Reference, or help etc",
        ),
    ] = None
    """
    URL to help remediate the problem, or provide more information, or to API Reference, or help etc
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
