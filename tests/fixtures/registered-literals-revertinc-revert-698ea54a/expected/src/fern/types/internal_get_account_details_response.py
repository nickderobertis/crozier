

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class InternalGetAccountDetailsResponse(UniversalBaseModel):
    account: "CommonAccount"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .common_account import CommonAccount
from .common_app import CommonApp
from .common_connection import CommonConnection
from .common_revert_user import CommonRevertUser

update_forward_refs(
    InternalGetAccountDetailsResponse,
    CommonAccount=CommonAccount,
    CommonApp=CommonApp,
    CommonConnection=CommonConnection,
    CommonRevertUser=CommonRevertUser,
)
