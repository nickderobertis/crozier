

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_error_data import ApiErrorData
from .message_aborted_error_data import MessageAbortedErrorData
from .message_output_length_error_data import MessageOutputLengthErrorData
from .provider_auth_error_data import ProviderAuthErrorData
from .unknown_error_data import UnknownErrorData


class EventSessionErrorPropertiesError_ProviderAuthError(UniversalBaseModel):
    name: typing.Literal["ProviderAuthError"] = "ProviderAuthError"
    data: ProviderAuthErrorData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EventSessionErrorPropertiesError_UnknownError(UniversalBaseModel):
    name: typing.Literal["UnknownError"] = "UnknownError"
    data: UnknownErrorData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EventSessionErrorPropertiesError_MessageOutputLengthError(UniversalBaseModel):
    name: typing.Literal["MessageOutputLengthError"] = "MessageOutputLengthError"
    data: MessageOutputLengthErrorData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EventSessionErrorPropertiesError_MessageAbortedError(UniversalBaseModel):
    name: typing.Literal["MessageAbortedError"] = "MessageAbortedError"
    data: MessageAbortedErrorData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EventSessionErrorPropertiesError_ApiError(UniversalBaseModel):
    name: typing.Literal["APIError"] = "APIError"
    data: ApiErrorData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


EventSessionErrorPropertiesError = typing_extensions.Annotated[
    typing.Union[
        EventSessionErrorPropertiesError_ProviderAuthError,
        EventSessionErrorPropertiesError_UnknownError,
        EventSessionErrorPropertiesError_MessageOutputLengthError,
        EventSessionErrorPropertiesError_MessageAbortedError,
        EventSessionErrorPropertiesError_ApiError,
    ],
    pydantic.Field(discriminator="name"),
]
