

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .postgres_subscribe_op_spec_columns import PostgresSubscribeOpSpecColumns
from .postgres_subscribe_op_spec_payload import PostgresSubscribeOpSpecPayload


class PostgresSubscribeOpSpec(UniversalBaseModel):
    columns: PostgresSubscribeOpSpecColumns
    payload: typing.Optional[PostgresSubscribeOpSpecPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
