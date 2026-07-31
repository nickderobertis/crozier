

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResponseApiKey(UniversalBaseModel):
    """
    Returned by `regenerate-api-key` (new key) and `clear-api-key`
    (apiKey: null). `apiKey` is the value to send as `X-Api-Key`.
    """

    api_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
