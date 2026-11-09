

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apply_update import ApplyUpdate
from .revert_update import RevertUpdate


class ConsensusUpdatesResponse(UniversalBaseModel):
    applied: typing.List[ApplyUpdate]
    reverted: typing.List[RevertUpdate]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
