

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_preconditioning_air_conditioning_programs_item import RemotePreconditioningAirConditioningProgramsItem


class RemotePreconditioningAirConditioning(UniversalBaseModel):
    """
    At least one of the parameters must be provided.
    """

    immediate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether air conditioning will start immediately or not independently if scheduled ```programs``` are set or not. Set to "false" by default.
    """

    programs: typing.Optional[typing.List[RemotePreconditioningAirConditioningProgramsItem]] = pydantic.Field(
        default=None
    )
    """
    List of air conditioning programs to schedule on vehicle.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
