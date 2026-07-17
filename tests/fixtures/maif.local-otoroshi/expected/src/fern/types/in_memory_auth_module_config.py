

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .in_memory_user import InMemoryUser


class InMemoryAuthModuleConfig(UniversalBaseModel):
    """
    Settings to authenticate users using the in memory user store
    """

    desc: str = pydantic.Field()
    """
    Description of the config
    """

    id: str = pydantic.Field()
    """
    Unique id of the config
    """

    name: str = pydantic.Field()
    """
    Name of the config
    """

    session_max_age: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sessionMaxAge"),
        pydantic.Field(alias="sessionMaxAge", description="Max age of the session"),
    ]
    """
    Max age of the session
    """

    type: str = pydantic.Field()
    """
    Type of settings. value is basic
    """

    users: typing.List[InMemoryUser] = pydantic.Field()
    """
    List of users
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
