

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .response import Response
from .response_page_mapping_data import ResponsePageMappingData


class ResponsePageMapping(Response):
    data: typing.Optional[ResponsePageMappingData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ResponsePageMapping)
