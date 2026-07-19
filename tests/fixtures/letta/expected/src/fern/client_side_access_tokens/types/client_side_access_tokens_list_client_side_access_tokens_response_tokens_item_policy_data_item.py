

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_access_item import (
    ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemAccessItem,
)
from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item_type import (
    ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemType,
)


class ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItem(UniversalBaseModel):
    type: ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemType
    id: str
    access: typing.List[ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemAccessItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
