

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxEnvironmentVariableUpdate(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the environment variable.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the environment variable.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of the environment variable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
