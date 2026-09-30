

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mssql_sel_perm import MssqlSelPerm


class MssqlSelectPermDef(UniversalBaseModel):
    comment: typing.Optional[str] = None
    permission: MssqlSelPerm
    role: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
