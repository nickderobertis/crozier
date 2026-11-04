

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AddProvider(UniversalBaseModel):
    """
    Will add a new provider or update an existing one with the same base docker image ID
    (docker registry + repository, excluding tag)
    """

    auto_stop_timeout_sec: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.
    """

    variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
