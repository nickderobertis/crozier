

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chainstate_tokens_response_data_item import ChainstateTokensResponseDataItem


class ChainstateTokensResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ChainstateTokensResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/accounts/#approval">Approval</a> or <a href="/data-model/chainstate/#token">Token</a> data. Corresponds to the <a href="/chifra/chainstate/#chifra-tokens">chifra tokens</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
