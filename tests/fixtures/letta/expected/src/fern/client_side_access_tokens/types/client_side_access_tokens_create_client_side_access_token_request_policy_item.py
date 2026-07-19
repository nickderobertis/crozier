

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_side_access_tokens_create_client_side_access_token_request_policy_item_access_item import (
    ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem,
)
from .client_side_access_tokens_create_client_side_access_token_request_policy_item_type import (
    ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType,
)


class ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem(UniversalBaseModel):
    type: ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType
    id: str
    access: typing.List[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
