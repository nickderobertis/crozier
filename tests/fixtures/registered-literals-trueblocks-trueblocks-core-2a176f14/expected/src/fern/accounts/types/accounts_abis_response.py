

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .accounts_abis_response_data_item import AccountsAbisResponseDataItem


class AccountsAbisResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AccountsAbisResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#abi">Abi</a>, <a href="/data-model/other/#function">Function</a> or <a href="/data-model/other/#parameter">Parameter</a> data. Corresponds to the <a href="/chifra/accounts/#chifra-abis">chifra abis</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(AccountsAbisResponse)
