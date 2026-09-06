

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quarantine_user_action_metadata import QuarantineUserActionMetadata


class QuarantineUserAction(UniversalBaseModel):
    type: int
    metadata: typing.Optional[QuarantineUserActionMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
