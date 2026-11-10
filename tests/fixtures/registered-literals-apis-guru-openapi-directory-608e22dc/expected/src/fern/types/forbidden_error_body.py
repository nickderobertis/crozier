

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors#unprovisioned"] = (
        "https://developer.nexmo.com/api-errors#unprovisioned"
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


class ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/subaccounts#invalid-number-transfer"] = (
        "https://developer.nexmo.com/api-errors/subaccounts#invalid-number-transfer"
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


ForbiddenErrorBody = typing_extensions.Annotated[
    typing.Union[
        ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned,
        ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer,
    ],
    pydantic.Field(discriminator="type"),
]
