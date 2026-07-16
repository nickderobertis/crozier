

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InMemoryUser(UniversalBaseModel):
    """
    A user
    """

    email: str = pydantic.Field()
    """
    Email of the user
    """

    metadata: typing.Dict[str, str] = pydantic.Field()
    """
    Metadata of the user
    """

    name: str = pydantic.Field()
    """
    Name of the user
    """

    password: str = pydantic.Field()
    """
    Password of the user (BCrypt hash)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
