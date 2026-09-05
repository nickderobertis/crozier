

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address_line_safe_str import AddressLineSafeStr
from .country_name_str import CountryNameStr
from .display_safe_str import DisplaySafeStr
from .postal_code_safe_str import PostalCodeSafeStr


class MyProfileAddressRestPatch(UniversalBaseModel):
    institution: typing.Optional[DisplaySafeStr] = None
    address: typing.Optional[AddressLineSafeStr] = None
    city: typing.Optional[DisplaySafeStr] = None
    state: typing.Optional[DisplaySafeStr] = None
    postal_code: typing_extensions.Annotated[
        typing.Optional[PostalCodeSafeStr], FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode")
    ] = None
    country: typing.Optional[CountryNameStr] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
