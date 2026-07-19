

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_config_update_config import SandboxConfigUpdateConfig


class SandboxConfigUpdate(UniversalBaseModel):
    """
    Pydantic model for updating SandboxConfig fields.
    """

    config: typing.Optional[SandboxConfigUpdateConfig] = pydantic.Field(default=None)
    """
    The JSON configuration data for the sandbox.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
