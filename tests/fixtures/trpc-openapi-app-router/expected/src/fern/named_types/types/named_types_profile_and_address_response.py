

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .named_types_profile_and_address_response_result import NamedTypesProfileAndAddressResponseResult


class NamedTypesProfileAndAddressResponse(UniversalBaseModel):
    result: NamedTypesProfileAndAddressResponseResult

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
