

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .accounts_monitors_response_data_item import AccountsMonitorsResponseDataItem


class AccountsMonitorsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AccountsMonitorsResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#message">Message</a>, <a href="/data-model/accounts/#monitor">Monitor</a> or <a href="/data-model/admin/#monitorclean">MonitorClean</a> data. Corresponds to the <a href="/chifra/accounts/#chifra-monitors">chifra monitors</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
