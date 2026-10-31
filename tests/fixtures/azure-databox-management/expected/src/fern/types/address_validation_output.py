

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address_validation_properties import AddressValidationProperties


class AddressValidationOutput(UniversalBaseModel):
    """
    Output of the address validation api.
    """

    properties: typing.Optional[AddressValidationProperties] = pydantic.Field(default=None)
    """
    The address validation properties.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
