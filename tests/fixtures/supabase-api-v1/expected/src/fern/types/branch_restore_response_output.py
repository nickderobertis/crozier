

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .branch_restore_response_output_message import BranchRestoreResponseOutputMessage


class BranchRestoreResponseOutput(UniversalBaseModel):
    message: BranchRestoreResponseOutputMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
