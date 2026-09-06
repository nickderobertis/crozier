

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .key_value import KeyValue


class EventActionCommandConfig(UniversalBaseModel):
    cmd: typing.Optional[str] = pydantic.Field(default=None)
    """
    absolute path to the command to execute
    """

    args: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    command line arguments
    """

    timeout: typing.Optional[int] = None
    env_vars: typing.Optional[typing.List[KeyValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
