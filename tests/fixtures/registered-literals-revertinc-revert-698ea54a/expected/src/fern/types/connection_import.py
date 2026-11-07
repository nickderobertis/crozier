

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_tpid import CommonTpid


class ConnectionImport(UniversalBaseModel):
    tp_id: CommonTpid
    tp_access_token: str
    tp_refresh_token: str
    tp_customer_id: str = pydantic.Field()
    """
    The emailId or a unique ID id of the user who connected the app.
    """

    t_id: str
    tp_account_url: typing.Optional[str] = None
    app_client_id: str
    app_client_secret: str
    app_id: str = pydantic.Field()
    """
    Can be obtained from the integration dashboard.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
