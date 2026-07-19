

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_data_item import (
    ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItem,
)
from .client_side_access_tokens_list_client_side_access_tokens_response_tokens_item_policy_version import (
    ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyVersion,
)


class ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicy(UniversalBaseModel):
    version: ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyVersion
    data: typing.List[ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
