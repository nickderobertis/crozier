

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .introspect_token_response_application import IntrospectTokenResponseApplication
from .introspect_token_response_authorization import IntrospectTokenResponseAuthorization


class IntrospectTokenResponse(UniversalBaseModel):
    authorization: typing.Optional[IntrospectTokenResponseAuthorization] = pydantic.Field(default=None)
    """
    The Authorization object
    """

    application: typing.Optional[IntrospectTokenResponseApplication] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
