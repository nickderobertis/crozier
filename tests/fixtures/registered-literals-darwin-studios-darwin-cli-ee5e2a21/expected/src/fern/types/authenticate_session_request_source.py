

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthenticateSessionRequestSource_OneTime(UniversalBaseModel):
    kind: typing.Literal["one_time"] = "one_time"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AuthenticateSessionRequestSource_DarwinVault(UniversalBaseModel):
    kind: typing.Literal["darwin_vault"] = "darwin_vault"
    vault_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaultItemId"), pydantic.Field(alias="vaultItemId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AuthenticateSessionRequestSource_ExternalVault(UniversalBaseModel):
    kind: typing.Literal["external_vault"] = "external_vault"
    vault_connection_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaultConnectionId"), pydantic.Field(alias="vaultConnectionId")
    ]
    item_reference: typing_extensions.Annotated[
        str, FieldMetadata(alias="itemReference"), pydantic.Field(alias="itemReference")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AuthenticateSessionRequestSource = typing_extensions.Annotated[
    typing.Union[
        AuthenticateSessionRequestSource_OneTime,
        AuthenticateSessionRequestSource_DarwinVault,
        AuthenticateSessionRequestSource_ExternalVault,
    ],
    pydantic.Field(discriminator="kind"),
]
