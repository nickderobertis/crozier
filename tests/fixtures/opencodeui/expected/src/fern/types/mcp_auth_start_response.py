

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class McpAuthStartResponse(UniversalBaseModel):
    authorization_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="authorizationUrl"),
        pydantic.Field(alias="authorizationUrl", description="URL to open in browser for authorization"),
    ]
    """
    URL to open in browser for authorization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
