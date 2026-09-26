

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_provider_resource_associations_register_response_not_applicable_reason import (
    PostInternalProviderResourceAssociationsRegisterResponseNotApplicableReason,
)


class PostInternalProviderResourceAssociationsRegisterResponse_Created(UniversalBaseModel):
    status: typing.Literal["created"] = "created"
    association_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="associationId"), pydantic.Field(alias="associationId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalProviderResourceAssociationsRegisterResponse_AlreadyExists(UniversalBaseModel):
    status: typing.Literal["already_exists"] = "already_exists"
    association_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="associationId"), pydantic.Field(alias="associationId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalProviderResourceAssociationsRegisterResponse_NotApplicable(UniversalBaseModel):
    status: typing.Literal["not_applicable"] = "not_applicable"
    reason: PostInternalProviderResourceAssociationsRegisterResponseNotApplicableReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalProviderResourceAssociationsRegisterResponse = typing_extensions.Annotated[
    typing.Union[
        PostInternalProviderResourceAssociationsRegisterResponse_Created,
        PostInternalProviderResourceAssociationsRegisterResponse_AlreadyExists,
        PostInternalProviderResourceAssociationsRegisterResponse_NotApplicable,
    ],
    pydantic.Field(discriminator="status"),
]
