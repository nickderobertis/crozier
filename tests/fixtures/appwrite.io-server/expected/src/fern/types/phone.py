

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Phone(UniversalBaseModel):
    """
    Phone
    """

    code: str = pydantic.Field()
    """
    Phone code.
    """

    country_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="Country two-character ISO 3166-1 alpha code."),
    ]
    """
    Country two-character ISO 3166-1 alpha code.
    """

    country_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="countryName"), pydantic.Field(alias="countryName", description="Country name.")
    ]
    """
    Country name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
