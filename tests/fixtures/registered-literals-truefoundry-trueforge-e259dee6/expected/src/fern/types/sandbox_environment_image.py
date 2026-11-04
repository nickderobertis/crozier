

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_environment_image_type import SandboxEnvironmentImageType


class SandboxEnvironmentImage(UniversalBaseModel):
    build_script: typing.Optional[str] = pydantic.Field(default=None)
    """
    Shell script used to build the snapshot.
    """

    type: SandboxEnvironmentImageType = pydantic.Field()
    """
    Build a snapshot from a script.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
