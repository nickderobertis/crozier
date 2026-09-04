

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AvailableModelProvider(UniversalBaseModel):
    """
    Owning configured provider.
    """

    name: str = pydantic.Field()
    """
    Configured provider resource name; matches the FQN prefix of `name`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
