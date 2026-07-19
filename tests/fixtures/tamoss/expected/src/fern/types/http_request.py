

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpRequest(UniversalBaseModel):
    """
    Gives information on a particular http request a client should perform
    """

    url: str = pydantic.Field()
    """
    The URL to make the request to. Where this URL is pre-signed, it SHALL remain valid for the timeframe advertised in [`min_presigned_url_timeout` at the `/service`](#/operations/GET_service) endpoint, which is subject to a specified minimum (see service endpoint schema).
    """

    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the body which needs to be included in the request
    """

    content_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="content-type"),
        pydantic.Field(alias="content-type", description="The content type which must be used"),
    ] = None
    """
    The content type which must be used
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Additional headers that should be included
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
