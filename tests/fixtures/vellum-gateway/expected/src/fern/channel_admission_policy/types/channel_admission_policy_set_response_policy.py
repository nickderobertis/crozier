

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .channel_admission_policy_set_response_policy_policy import ChannelAdmissionPolicySetResponsePolicyPolicy


class ChannelAdmissionPolicySetResponsePolicy(UniversalBaseModel):
    channel_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="channelType"), pydantic.Field(alias="channelType")
    ]
    policy: ChannelAdmissionPolicySetResponsePolicyPolicy
    note: typing.Optional[str] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
