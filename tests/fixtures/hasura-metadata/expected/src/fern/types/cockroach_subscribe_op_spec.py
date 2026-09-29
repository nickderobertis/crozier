

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cockroach_subscribe_op_spec_columns import CockroachSubscribeOpSpecColumns
from .cockroach_subscribe_op_spec_payload import CockroachSubscribeOpSpecPayload


class CockroachSubscribeOpSpec(UniversalBaseModel):
    columns: CockroachSubscribeOpSpecColumns
    payload: typing.Optional[CockroachSubscribeOpSpecPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
