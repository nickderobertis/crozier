

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_run_status_response_output_message import UpdateRunStatusResponseOutputMessage


class UpdateRunStatusResponseOutput(UniversalBaseModel):
    message: UpdateRunStatusResponseOutputMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
