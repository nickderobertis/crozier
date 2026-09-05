

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_env_var import ContainerEnvVar


class ContainerProcess(UniversalBaseModel):
    """
    Container process configuration
    """

    command: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entrypoint override
    """

    args: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Arguments to the entrypoint
    """

    env: typing.Optional[typing.List[ContainerEnvVar]] = pydantic.Field(default=None)
    """
    Environment variables
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
