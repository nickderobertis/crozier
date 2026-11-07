

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .common_app_config import CommonAppConfig
from .common_tpid import CommonTpid


class CommonApp(UniversalBaseModel):
    id: str
    tp_id: CommonTpid
    scope: typing.Optional[typing.List[str]] = None
    available_scope: typing.List[str]
    app_client_id: typing.Optional[str] = None
    app_client_secret: typing.Optional[str] = None
    owner_account_public_token: str
    account: typing.Optional["CommonAccount"] = None
    connections: typing.Optional[typing.List["CommonConnection"]] = None
    is_revert_app: bool
    app_config: typing.Optional[CommonAppConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .common_account import CommonAccount
from .common_connection import CommonConnection
from .common_revert_user import CommonRevertUser

update_forward_refs(
    CommonApp, CommonAccount=CommonAccount, CommonConnection=CommonConnection, CommonRevertUser=CommonRevertUser
)
