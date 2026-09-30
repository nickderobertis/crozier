

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mssql_subscribe_op_spec import MssqlSubscribeOpSpec


class MssqlTriggerOpsDef(UniversalBaseModel):
    delete: typing.Optional[MssqlSubscribeOpSpec] = None
    enable_manual: typing.Optional[bool] = None
    insert: typing.Optional[MssqlSubscribeOpSpec] = None
    update: typing.Optional[MssqlSubscribeOpSpec] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
