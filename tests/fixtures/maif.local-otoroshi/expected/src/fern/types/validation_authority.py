

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ValidationAuthority(UniversalBaseModel):
    """
    Settings to access a validation authority server
    """

    always_valid: typing_extensions.Annotated[bool, FieldMetadata(alias="alwaysValid")] = pydantic.Field()
    """
    Bypass http calls, every certificates are valids
    """

    bad_ttl: typing_extensions.Annotated[int, FieldMetadata(alias="badTtl")] = pydantic.Field()
    """
    The TTL for invalid access response caching
    """

    description: str = pydantic.Field()
    """
    The description of the settings
    """

    good_ttl: typing_extensions.Annotated[int, FieldMetadata(alias="goodTtl")] = pydantic.Field()
    """
    The TTL for valid access response caching
    """

    headers: typing.Dict[str, str] = pydantic.Field()
    """
    HTTP call headers
    """

    host: str = pydantic.Field()
    """
    The host of the server
    """

    id: str = pydantic.Field()
    """
    The id of the settings
    """

    method: str = pydantic.Field()
    """
    The HTTP method
    """

    name: str = pydantic.Field()
    """
    The name of the settings
    """

    no_cache: typing_extensions.Annotated[bool, FieldMetadata(alias="noCache")] = pydantic.Field()
    """
    Avoid caching responses
    """

    path: str = pydantic.Field()
    """
    The URL path
    """

    timeout: int = pydantic.Field()
    """
    The call timeout
    """

    url: str = pydantic.Field()
    """
    The URL of the server
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
