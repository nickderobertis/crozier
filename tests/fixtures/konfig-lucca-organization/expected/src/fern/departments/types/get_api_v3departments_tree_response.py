

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .get_api_v3departments_tree_response_data import GetApiV3DepartmentsTreeResponseData


class GetApiV3DepartmentsTreeResponse(UniversalBaseModel):
    data: typing.Optional[GetApiV3DepartmentsTreeResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetApiV3DepartmentsTreeResponse)
