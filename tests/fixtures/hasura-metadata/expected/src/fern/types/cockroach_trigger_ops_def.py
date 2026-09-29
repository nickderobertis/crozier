

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cockroach_subscribe_op_spec import CockroachSubscribeOpSpec


class CockroachTriggerOpsDef(UniversalBaseModel):
    delete: typing.Optional[CockroachSubscribeOpSpec] = None
    enable_manual: typing.Optional[bool] = None
    insert: typing.Optional[CockroachSubscribeOpSpec] = None
    update: typing.Optional[CockroachSubscribeOpSpec] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
