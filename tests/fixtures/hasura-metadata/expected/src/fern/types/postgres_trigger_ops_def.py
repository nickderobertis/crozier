

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .postgres_subscribe_op_spec import PostgresSubscribeOpSpec


class PostgresTriggerOpsDef(UniversalBaseModel):
    delete: typing.Optional[PostgresSubscribeOpSpec] = None
    enable_manual: typing.Optional[bool] = None
    insert: typing.Optional[PostgresSubscribeOpSpec] = None
    update: typing.Optional[PostgresSubscribeOpSpec] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
