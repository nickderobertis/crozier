

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .citus_subscribe_op_spec import CitusSubscribeOpSpec


class CitusTriggerOpsDef(UniversalBaseModel):
    delete: typing.Optional[CitusSubscribeOpSpec] = None
    enable_manual: typing.Optional[bool] = None
    insert: typing.Optional[CitusSubscribeOpSpec] = None
    update: typing.Optional[CitusSubscribeOpSpec] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
