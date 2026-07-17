

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CorsSettings(UniversalBaseModel):
    """
    The configuration for cors support
    """

    allow_credentials: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="allowCredentials"),
        pydantic.Field(alias="allowCredentials", description="Allow to pass credentials"),
    ]
    """
    Allow to pass credentials
    """

    allow_headers: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="allowHeaders"),
        pydantic.Field(alias="allowHeaders", description="The cors allowed headers"),
    ]
    """
    The cors allowed headers
    """

    allow_methods: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="allowMethods"),
        pydantic.Field(alias="allowMethods", description="The cors allowed methods"),
    ]
    """
    The cors allowed methods
    """

    allow_origin: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="allowOrigin"),
        pydantic.Field(alias="allowOrigin", description="The cors allowed origin"),
    ]
    """
    The cors allowed origin
    """

    enabled: bool = pydantic.Field()
    """
    Whether or not cors is enabled
    """

    excluded_patterns: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="excludedPatterns"),
        pydantic.Field(alias="excludedPatterns", description="The cors excluded patterns"),
    ]
    """
    The cors excluded patterns
    """

    expose_headers: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="exposeHeaders"),
        pydantic.Field(alias="exposeHeaders", description="The cors exposed header"),
    ]
    """
    The cors exposed header
    """

    max_age: typing_extensions.Annotated[
        int, FieldMetadata(alias="maxAge"), pydantic.Field(alias="maxAge", description="Cors max age")
    ]
    """
    Cors max age
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
