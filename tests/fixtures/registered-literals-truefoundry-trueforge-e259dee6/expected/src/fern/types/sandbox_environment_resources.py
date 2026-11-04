

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxEnvironmentResources(UniversalBaseModel):
    cpu: typing.Optional[float] = pydantic.Field(default=None)
    """
    CPU allocation in cores.
    """

    disk: typing.Optional[float] = pydantic.Field(default=None)
    """
    Disk allocation in GiB.
    """

    memory: typing.Optional[float] = pydantic.Field(default=None)
    """
    Memory allocation in GiB.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
