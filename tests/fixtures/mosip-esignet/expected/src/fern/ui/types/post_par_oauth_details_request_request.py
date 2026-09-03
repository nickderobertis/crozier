

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostParOauthDetailsRequestRequest(UniversalBaseModel):
    request_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="requestUri"),
        pydantic.Field(
            alias="requestUri",
            description="The request URI corresponding to the authorization request posted. This URI is a single-use reference to the respective request data in the subsequent authorization request.",
        ),
    ]
    """
    The request URI corresponding to the authorization request posted. This URI is a single-use reference to the respective request data in the subsequent authorization request.
    """

    client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId", description="The client identifier")
    ]
    """
    The client identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
