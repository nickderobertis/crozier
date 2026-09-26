

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OnboardCapabilitiesRemoteChargingParametersImmediate(UniversalBaseModel):
    start: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true means remote immediate charge start action is supported.
    """

    stop: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true means remote immediate charge stop action is supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
