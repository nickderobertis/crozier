

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .branch_delete_response_output_message import BranchDeleteResponseOutputMessage


class BranchDeleteResponseOutput(UniversalBaseModel):
    message: BranchDeleteResponseOutputMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
