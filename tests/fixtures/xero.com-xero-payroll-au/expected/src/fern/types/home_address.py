

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .state import State


class HomeAddress(UniversalBaseModel):
    address_line1: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AddressLine1"),
        pydantic.Field(alias="AddressLine1", description="Address line 1 for employee home address"),
    ]
    """
    Address line 1 for employee home address
    """

    address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AddressLine2"),
        pydantic.Field(alias="AddressLine2", description="Address line 2 for employee home address"),
    ] = None
    """
    Address line 2 for employee home address
    """

    city: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="City"),
        pydantic.Field(alias="City", description="Suburb for employee home address"),
    ] = None
    """
    Suburb for employee home address
    """

    country: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Country"),
        pydantic.Field(alias="Country", description="Country of HomeAddress"),
    ] = None
    """
    Country of HomeAddress
    """

    postal_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PostalCode"),
        pydantic.Field(alias="PostalCode", description="PostCode for employee home address"),
    ] = None
    """
    PostCode for employee home address
    """

    region: typing_extensions.Annotated[
        typing.Optional[State], FieldMetadata(alias="Region"), pydantic.Field(alias="Region")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
