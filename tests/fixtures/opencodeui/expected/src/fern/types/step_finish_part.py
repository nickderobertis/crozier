

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .step_finish_part_tokens import StepFinishPartTokens


class StepFinishPart(UniversalBaseModel):
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    reason: str
    snapshot: typing.Optional[str] = None
    cost: float
    tokens: StepFinishPartTokens

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
