

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_channel_params_invalid_parameters_item import ErrorChannelParamsInvalidParametersItem
from .error_message_params_invalid_parameters_item import ErrorMessageParamsInvalidParametersItem


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsInvalidJson(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors#invalid-json"] = (
        "https://developer.nexmo.com/api-errors#invalid-json"
    )
    detail: str
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1100(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/messages-olympus#1100"] = (
        "https://developer.nexmo.com/api-errors/messages-olympus#1100"
    )
    detail: str
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1110(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/messages-olympus#1110"] = (
        "https://developer.nexmo.com/api-errors/messages-olympus#1110"
    )
    detail: str
    instance: str
    invalid_parameters: typing.Optional[typing.List[ErrorChannelParamsInvalidParametersItem]] = None
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1120(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/messages-olympus#1120"] = (
        "https://developer.nexmo.com/api-errors/messages-olympus#1120"
    )
    detail: str
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus110(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/messages-olympus#110"] = (
        "https://developer.nexmo.com/api-errors/messages-olympus#110"
    )
    detail: str
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1140(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/messages-olympus#1140"] = (
        "https://developer.nexmo.com/api-errors/messages-olympus#1140"
    )
    detail: str
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1150(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/messages-olympus#1150"] = (
        "https://developer.nexmo.com/api-errors/messages-olympus#1150"
    )
    detail: str
    instance: str
    invalid_parameters: typing.Optional[typing.List[ErrorMessageParamsInvalidParametersItem]] = None
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1060(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/messages-olympus#1060"] = (
        "https://developer.nexmo.com/api-errors/messages-olympus#1060"
    )
    detail: str
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UnprocessableEntityErrorBody = typing_extensions.Annotated[
    typing.Union[
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsInvalidJson,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1100,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1110,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1120,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus110,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1140,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1150,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1060,
    ],
    pydantic.Field(discriminator="type"),
]
