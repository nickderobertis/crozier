

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .citus_subscribe_op_spec_columns import CitusSubscribeOpSpecColumns
from .citus_subscribe_op_spec_payload import CitusSubscribeOpSpecPayload


class CitusSubscribeOpSpec(UniversalBaseModel):
    columns: CitusSubscribeOpSpecColumns
    payload: typing.Optional[CitusSubscribeOpSpecPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
