

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .common_tpid import CommonTpid


class CommonConnection(UniversalBaseModel):
    tp_id: CommonTpid
    tp_access_token: str
    tp_refresh_token: typing.Optional[str] = None
    tp_customer_id: str
    t_id: str
    tp_account_url: typing.Optional[str] = None
    owner_account_public_token: str
    app_client_id: typing.Optional[str] = None
    app_client_secret: typing.Optional[str] = None
    app: typing.Optional["CommonApp"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .common_account import CommonAccount
from .common_app import CommonApp
from .common_revert_user import CommonRevertUser

update_forward_refs(
    CommonConnection, CommonAccount=CommonAccount, CommonApp=CommonApp, CommonRevertUser=CommonRevertUser
)
