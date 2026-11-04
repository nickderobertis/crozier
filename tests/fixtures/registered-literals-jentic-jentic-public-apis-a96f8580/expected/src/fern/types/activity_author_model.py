

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ActivityAuthorModel_InternalUser(UniversalBaseModel):
    type: typing.Literal["internalUser"] = "internalUser"
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    email: str
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    company_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="companyName"), pydantic.Field(alias="companyName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActivityAuthorModel_ExternalUser(UniversalBaseModel):
    type: typing.Literal["externalUser"] = "externalUser"
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    email: str
    company_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="companyName"), pydantic.Field(alias="companyName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActivityAuthorModel_Integration(UniversalBaseModel):
    type: typing.Literal["integration"] = "integration"
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActivityAuthorModel_System(UniversalBaseModel):
    type: typing.Literal["system"] = "system"
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ActivityAuthorModel = typing_extensions.Annotated[
    typing.Union[
        ActivityAuthorModel_InternalUser,
        ActivityAuthorModel_ExternalUser,
        ActivityAuthorModel_Integration,
        ActivityAuthorModel_System,
    ],
    pydantic.Field(discriminator="type"),
]
