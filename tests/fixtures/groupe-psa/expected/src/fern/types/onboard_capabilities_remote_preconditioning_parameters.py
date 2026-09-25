

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .onboard_capabilities_remote_preconditioning_parameters_programs import (
    OnboardCapabilitiesRemotePreconditioningParametersPrograms,
)


class OnboardCapabilitiesRemotePreconditioningParameters(UniversalBaseModel):
    programs: typing.Optional[OnboardCapabilitiesRemotePreconditioningParametersPrograms] = None
    immediate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true means remote preconditioning immediate action is supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
