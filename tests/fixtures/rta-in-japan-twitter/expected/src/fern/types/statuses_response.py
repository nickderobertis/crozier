

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class StatusesResponse(UniversalBaseModel):
    code: typing.Optional[int] = None
    data: typing.Optional[typing.List["Statuses"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .statuses import Statuses

update_forward_refs(StatusesResponse, Statuses=Statuses)
