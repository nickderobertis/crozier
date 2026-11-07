

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .act_update_request_completion_completion import ActUpdateRequestCompletionCompletion
from .act_update_request_completion_cooperation import ActUpdateRequestCompletionCooperation
from .act_update_request_completion_correctness import ActUpdateRequestCompletionCorrectness
from .act_update_request_completion_kind import ActUpdateRequestCompletionKind
from .act_update_request_completion_safety import ActUpdateRequestCompletionSafety
from .act_update_request_completion_timeliness import ActUpdateRequestCompletionTimeliness


class ActUpdateRequestCompletion(UniversalBaseModel):
    kind: ActUpdateRequestCompletionKind
    interaction_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="interactionId"), pydantic.Field(alias="interactionId")
    ]
    expected_revision: typing_extensions.Annotated[
        int, FieldMetadata(alias="expectedRevision"), pydantic.Field(alias="expectedRevision")
    ]
    completion: ActUpdateRequestCompletionCompletion
    correctness: ActUpdateRequestCompletionCorrectness
    timeliness: ActUpdateRequestCompletionTimeliness
    cooperation: ActUpdateRequestCompletionCooperation
    safety: ActUpdateRequestCompletionSafety
    reason_codes: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="reasonCodes"), pydantic.Field(alias="reasonCodes")
    ]
    note: typing.Optional[str] = None
    request_id: typing_extensions.Annotated[str, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
