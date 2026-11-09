

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetDeviceEnvironmentVariablesByPinResponse(UniversalBaseModel):
    environment_variable_notes: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Optional per-variable annotations for device-level environment variables, keyed by variable name.
    """

    environment_variables: typing.Dict[str, str] = pydantic.Field()
    """
    The environment variables for this device that have been set using host firmware or the Notehub API or UI.
    """

    environment_variables_effective: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The environment variables as they will be seen by the device, fully resolved with project/fleet/device prioritization rules.
    """

    environment_variables_env_default: typing.Dict[str, str] = pydantic.Field()
    """
    The environment variables that have been set using the env.default request through the Notecard API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
