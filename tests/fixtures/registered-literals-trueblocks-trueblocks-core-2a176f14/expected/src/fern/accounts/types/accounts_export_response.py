

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .accounts_export_response_data_item import AccountsExportResponseDataItem


class AccountsExportResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AccountsExportResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/accounts/#appearance">Appearance</a>, <a href="/data-model/other/#function">Function</a>, <a href="/data-model/chaindata/#log">Log</a>, <a href="/data-model/other/#message">Message</a>, <a href="/data-model/accounts/#monitor">Monitor</a>, <a href="/data-model/other/#parameter">Parameter</a>, <a href="/data-model/chaindata/#receipt">Receipt</a>, <a href="/data-model/accounts/#statement">Statement</a>, <a href="/data-model/chainstate/#token">Token</a>, <a href="/data-model/chaindata/#trace">Trace</a>, <a href="/data-model/chaindata/#traceaction">TraceAction</a>, <a href="/data-model/chaindata/#traceresult">TraceResult</a>, <a href="/data-model/chaindata/#transaction">Transaction</a>, <a href="/data-model/accounts/#transfer">Transfer</a> or <a href="/data-model/chaindata/#withdrawal">Withdrawal</a> data. Corresponds to the <a href="/chifra/accounts/#chifra-export">chifra export</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(AccountsExportResponse)
