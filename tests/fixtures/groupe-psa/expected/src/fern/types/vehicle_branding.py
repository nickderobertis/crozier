

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VehicleBranding(UniversalBaseModel):
    brand: typing.Optional[str] = pydantic.Field(default=None)
    """
    Brand of a vehicle
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Car model description.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
