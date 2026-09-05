

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DateRange(UniversalBaseModel):
    """
    Trade Policy Fixed Price Validity Period Object.
    """

    from_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="from"),
        pydantic.Field(
            alias="from", description="Indicates the date and time when the fixed price will start to be valid."
        ),
    ]
    """
    Indicates the date and time when the fixed price will start to be valid.
    """

    to: str = pydantic.Field()
    """
    Indicates the date and time from which the fixed price will no longer be valid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
