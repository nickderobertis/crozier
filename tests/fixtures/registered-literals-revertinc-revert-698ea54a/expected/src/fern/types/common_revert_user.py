

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class CommonRevertUser(UniversalBaseModel):
    id: str
    domain: str
    email: str
    account_id: typing_extensions.Annotated[str, FieldMetadata(alias="accountId"), pydantic.Field(alias="accountId")]
    account: typing.Optional["CommonAccount"] = None

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

update_forward_refs(
    CommonRevertUser, CommonAccount=CommonAccount, CommonApp=CommonApp, CommonConnection=CommonConnection
)
