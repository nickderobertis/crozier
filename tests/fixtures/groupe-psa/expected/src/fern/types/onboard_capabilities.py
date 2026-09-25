

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .onboard_capabilities_data_item import OnboardCapabilitiesDataItem
from .onboard_capabilities_remote import OnboardCapabilitiesRemote


class OnboardCapabilities(UniversalBaseModel):
    data: typing.Optional[typing.List[OnboardCapabilitiesDataItem]] = pydantic.Field(default=None)
    """
    List of retrievable data represented by their scopes.
    """

    remote: typing.Optional[OnboardCapabilitiesRemote] = pydantic.Field(default=None)
    """
    List of callable remote functions and associated supported properties.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
