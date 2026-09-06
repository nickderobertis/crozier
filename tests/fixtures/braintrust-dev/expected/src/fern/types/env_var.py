

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .env_var_object_type import EnvVarObjectType
from .env_var_secret_category import EnvVarSecretCategory


class EnvVar(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the environment variable
    """

    object_type: EnvVarObjectType = pydantic.Field()
    """
    The type of the object the environment variable is scoped for
    """

    object_id: str = pydantic.Field()
    """
    The id of the object the environment variable is scoped for
    """

    name: str = pydantic.Field()
    """
    The name of the environment variable
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of environment variable creation
    """

    used: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date the environment variable was last used
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional metadata associated with the environment variable when managed via the function secrets API
    """

    secret_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional classification for the secret (for example, the AI provider name)
    """

    secret_category: typing.Optional[EnvVarSecretCategory] = pydantic.Field(default=None)
    """
    The category of the secret: env_var for regular environment variables, ai_provider for AI provider API keys
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
