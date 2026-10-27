

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_message_policy_violation_dlp_action import ChatMessagePolicyViolationDlpAction
from .chat_message_policy_violation_policy_tip import ChatMessagePolicyViolationPolicyTip
from .chat_message_policy_violation_user_action import ChatMessagePolicyViolationUserAction
from .chat_message_policy_violation_verdict_details import ChatMessagePolicyViolationVerdictDetails


class ChatMessagePolicyViolation(UniversalBaseModel):
    dlp_action: typing_extensions.Annotated[
        typing.Optional[ChatMessagePolicyViolationDlpAction],
        FieldMetadata(alias="dlpAction"),
        pydantic.Field(alias="dlpAction"),
    ] = None
    justification_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="justificationText"), pydantic.Field(alias="justificationText")
    ] = None
    policy_tip: typing_extensions.Annotated[
        typing.Optional[ChatMessagePolicyViolationPolicyTip],
        FieldMetadata(alias="policyTip"),
        pydantic.Field(alias="policyTip"),
    ] = None
    user_action: typing_extensions.Annotated[
        typing.Optional[ChatMessagePolicyViolationUserAction],
        FieldMetadata(alias="userAction"),
        pydantic.Field(alias="userAction"),
    ] = None
    verdict_details: typing_extensions.Annotated[
        typing.Optional[ChatMessagePolicyViolationVerdictDetails],
        FieldMetadata(alias="verdictDetails"),
        pydantic.Field(alias="verdictDetails"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
