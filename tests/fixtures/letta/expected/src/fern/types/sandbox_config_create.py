

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_config_create_config import SandboxConfigCreateConfig


class SandboxConfigCreate(UniversalBaseModel):
    config: SandboxConfigCreateConfig = pydantic.Field()
    """
    The configuration for the sandbox.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
