

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multi_party_authorize_request_authorization_authorizations_item import (
    MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem,
)
from .multi_party_authorize_request_authorization_operation import MultiPartyAuthorizeRequestAuthorizationOperation
from .multi_party_authorize_request_authorization_type import MultiPartyAuthorizeRequestAuthorizationType


class MultiPartyAuthorizeRequestAuthorization(UniversalBaseModel):
    type: MultiPartyAuthorizeRequestAuthorizationType
    operation: MultiPartyAuthorizeRequestAuthorizationOperation
    required_parties: typing.Optional[int] = None
    authorizations: typing.List[MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
