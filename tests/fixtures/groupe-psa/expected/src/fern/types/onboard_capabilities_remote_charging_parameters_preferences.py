

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OnboardCapabilitiesRemoteChargingParametersPreferences(UniversalBaseModel):
    level: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true means remote charging preferences[level] is supported.
    """

    type: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true means remote charging preferences[type] is supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
