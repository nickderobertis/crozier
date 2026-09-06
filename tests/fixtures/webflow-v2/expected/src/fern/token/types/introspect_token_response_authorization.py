

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .introspect_token_response_authorization_authorized_to import IntrospectTokenResponseAuthorizationAuthorizedTo


class IntrospectTokenResponseAuthorization(UniversalBaseModel):
    """
    The Authorization object
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the Authorization instance
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the Authorization was created"),
    ] = None
    """
    The date the Authorization was created
    """

    last_used: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUsed"),
        pydantic.Field(alias="lastUsed", description="The date the Authorization was last used"),
    ] = None
    """
    The date the Authorization was last used
    """

    grant_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="grantType"),
        pydantic.Field(alias="grantType", description="The grant type of the Authorization"),
    ] = None
    """
    The grant type of the Authorization
    """

    rate_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rateLimit"),
        pydantic.Field(alias="rateLimit", description="The default rate limit for the Authorization (requests/min)"),
    ] = None
    """
    The default rate limit for the Authorization (requests/min)
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma separted list of OAuth scopes corresponding to the Authorization
    """

    authorized_to: typing_extensions.Annotated[
        typing.Optional[IntrospectTokenResponseAuthorizationAuthorizedTo],
        FieldMetadata(alias="authorizedTo"),
        pydantic.Field(alias="authorizedTo"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
