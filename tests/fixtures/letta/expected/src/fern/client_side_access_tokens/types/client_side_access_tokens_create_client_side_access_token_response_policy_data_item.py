

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_side_access_tokens_create_client_side_access_token_response_policy_data_item_access_item import (
    ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem,
)
from .client_side_access_tokens_create_client_side_access_token_response_policy_data_item_type import (
    ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemType,
)


class ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItem(UniversalBaseModel):
    type: ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemType
    id: str
    access: typing.List[ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
