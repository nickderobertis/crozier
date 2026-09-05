

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiKeyCreateResponse(UniversalBaseModel):
    id: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    expiration: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time delta from creation time to expiration. If None, then it does not expire.
    """

    api_base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiBaseUrl"), pydantic.Field(alias="apiBaseUrl")
    ] = None
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")]
    api_secret: typing_extensions.Annotated[str, FieldMetadata(alias="apiSecret"), pydantic.Field(alias="apiSecret")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
