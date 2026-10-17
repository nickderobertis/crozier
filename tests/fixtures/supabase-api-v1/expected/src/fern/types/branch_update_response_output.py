

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .branch_update_response_output_message import BranchUpdateResponseOutputMessage


class BranchUpdateResponseOutput(UniversalBaseModel):
    workflow_run_id: str
    message: BranchUpdateResponseOutputMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
