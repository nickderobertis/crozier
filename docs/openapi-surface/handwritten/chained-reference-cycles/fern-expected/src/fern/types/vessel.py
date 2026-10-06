

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Vessel(UniversalBaseModel):
    hull: typing.Optional[str] = None
    skipper: typing.Optional["Captain"] = None
    homeport: typing.Optional["Harbor"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .captain import Captain
from .harbor import Harbor

update_forward_refs(Vessel, Captain=Captain, Harbor=Harbor)
