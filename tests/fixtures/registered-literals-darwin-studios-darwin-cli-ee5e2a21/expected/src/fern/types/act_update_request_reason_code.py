

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .act_update_request_reason_code_kind import ActUpdateRequestReasonCodeKind
from .act_update_request_reason_code_reason_code import ActUpdateRequestReasonCodeReasonCode
from .act_update_request_reason_code_subject_role import ActUpdateRequestReasonCodeSubjectRole


class ActUpdateRequestReasonCode(UniversalBaseModel):
    kind: ActUpdateRequestReasonCodeKind
    reason_code: typing_extensions.Annotated[
        ActUpdateRequestReasonCodeReasonCode, FieldMetadata(alias="reasonCode"), pydantic.Field(alias="reasonCode")
    ]
    subject_role: typing_extensions.Annotated[
        typing.Optional[ActUpdateRequestReasonCodeSubjectRole],
        FieldMetadata(alias="subjectRole"),
        pydantic.Field(alias="subjectRole"),
    ] = None
    note: typing.Optional[str] = None
    request_id: typing_extensions.Annotated[str, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
