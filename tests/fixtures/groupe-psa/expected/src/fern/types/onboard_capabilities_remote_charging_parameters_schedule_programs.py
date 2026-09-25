

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OnboardCapabilitiesRemoteChargingParametersSchedulePrograms(UniversalBaseModel):
    supported: bool = pydantic.Field()
    """
    true means remote charging schedule[programs] is supported.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max number of program accepted by the vehicle.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
