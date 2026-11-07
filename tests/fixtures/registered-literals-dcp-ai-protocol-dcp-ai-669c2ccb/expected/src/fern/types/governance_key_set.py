

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .key_entry_v2 import KeyEntryV2


class GovernanceKeySet(UniversalBaseModel):
    governance_id: str
    keys: typing.List[KeyEntryV2]
    threshold: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
