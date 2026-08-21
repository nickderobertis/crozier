

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_v1traces_response_result_item_item import PutV1TracesResponseResultItemItem


class PutV1TracesResponse(UniversalBaseModel):
    result: typing.Optional[typing.List[typing.List[PutV1TracesResponseResultItemItem]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
