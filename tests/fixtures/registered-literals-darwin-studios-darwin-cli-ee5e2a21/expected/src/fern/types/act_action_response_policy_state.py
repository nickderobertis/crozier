

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .act_action_response_policy_state_code import ActActionResponsePolicyStateCode
from .act_action_response_policy_state_scope import ActActionResponsePolicyStateScope
from .act_action_response_policy_state_state import ActActionResponsePolicyStateState


class ActActionResponsePolicyState(UniversalBaseModel):
    state: ActActionResponsePolicyStateState
    code: ActActionResponsePolicyStateCode
    scope: ActActionResponsePolicyStateScope
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    web_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webLink"), pydantic.Field(alias="webLink")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
