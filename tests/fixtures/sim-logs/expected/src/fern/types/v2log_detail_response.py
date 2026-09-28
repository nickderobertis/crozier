

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .v2log_detail import V2LogDetail


class V2LogDetailResponse(UniversalBaseModel):
    """
    The complete diagnostic representation of a workflow run.
    """

    data: V2LogDetail = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(V2LogDetailResponse)
