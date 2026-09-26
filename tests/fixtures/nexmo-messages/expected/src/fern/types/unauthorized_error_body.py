

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnathorized(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/#unathorized"] = (
        "https://developer.nexmo.com/api-errors/#unathorized"
    )
    detail: typing.Optional[str] = None
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned(UniversalBaseModel):
    type: typing.Literal["https://developer.nexmo.com/api-errors/#unprovisioned"] = (
        "https://developer.nexmo.com/api-errors/#unprovisioned"
    )
    detail: typing.Optional[str] = None
    instance: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UnauthorizedErrorBody = typing_extensions.Annotated[
    typing.Union[
        UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnathorized,
        UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned,
    ],
    pydantic.Field(discriminator="type"),
]
