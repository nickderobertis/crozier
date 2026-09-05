

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quarantine_user_action_metadata_response import QuarantineUserActionMetadataResponse


class QuarantineUserActionResponse(UniversalBaseModel):
    type: int
    metadata: QuarantineUserActionMetadataResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
