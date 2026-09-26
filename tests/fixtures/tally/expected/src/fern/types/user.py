

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_subscription_plan import UserSubscriptionPlan


class User(UniversalBaseModel):
    id: typing.Optional[str] = None
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    full_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fullName"), pydantic.Field(alias="fullName")
    ] = None
    email: typing.Optional[str] = None
    avatar_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="avatarUrl"), pydantic.Field(alias="avatarUrl")
    ] = None
    organization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ] = None
    is_deleted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")
    ] = None
    has_two_factor_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasTwoFactorEnabled"), pydantic.Field(alias="hasTwoFactorEnabled")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    subscription_plan: typing_extensions.Annotated[
        typing.Optional[UserSubscriptionPlan],
        FieldMetadata(alias="subscriptionPlan"),
        pydantic.Field(alias="subscriptionPlan"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
