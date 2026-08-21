

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_v1traces_request_item_trace import PutV1TracesRequestItemTrace


class PutV1TracesRequestItem(UniversalBaseModel):
    trace: typing.Optional[PutV1TracesRequestItemTrace] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
