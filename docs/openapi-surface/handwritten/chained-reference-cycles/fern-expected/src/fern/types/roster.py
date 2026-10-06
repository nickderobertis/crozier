

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Roster(UniversalBaseModel):
    season: typing.Optional[str] = None
    captain: typing.Optional["Captain"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .captain import Captain
from .vessel import Vessel

update_forward_refs(Roster, Captain=Captain, Vessel=Vessel)
