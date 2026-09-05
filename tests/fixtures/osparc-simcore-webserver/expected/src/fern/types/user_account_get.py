

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_request_status import AccountRequestStatus
from .lower_case_email_str import LowerCaseEmailStr
from .primary_group_id import PrimaryGroupId
from .user_id_int import UserIdInt
from .user_name_id_str import UserNameIdStr
from .user_status import UserStatus


class UserAccountGet(UniversalBaseModel):
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    email: LowerCaseEmailStr
    institution: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    address: typing.Optional[str] = None
    city: typing.Optional[str] = None
    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State, province, canton, ...
    """

    postal_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode")
    ] = None
    country: typing.Optional[str] = None
    product_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="productName"), pydantic.Field(alias="productName")
    ] = None
    extras: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Keeps extra information provided in the request form
    """

    pre_registration_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="preRegistrationId"), pydantic.Field(alias="preRegistrationId")
    ] = None
    pre_registration_created: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="preRegistrationCreated"),
        pydantic.Field(alias="preRegistrationCreated"),
    ] = None
    invited_by: typing_extensions.Annotated[
        typing.Optional[UserNameIdStr], FieldMetadata(alias="invitedBy"), pydantic.Field(alias="invitedBy")
    ] = None
    account_request_status: typing_extensions.Annotated[
        typing.Optional[AccountRequestStatus],
        FieldMetadata(alias="accountRequestStatus"),
        pydantic.Field(alias="accountRequestStatus"),
    ] = None
    account_request_reviewed_by: typing_extensions.Annotated[
        typing.Optional[UserNameIdStr],
        FieldMetadata(alias="accountRequestReviewedBy"),
        pydantic.Field(alias="accountRequestReviewedBy"),
    ] = None
    account_request_reviewed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="accountRequestReviewedAt"),
        pydantic.Field(alias="accountRequestReviewedAt"),
    ] = None
    registered: bool
    status: typing.Optional[UserStatus] = None
    products: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of products this users is included or None if fields is unset
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[UserIdInt],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="Unique identifier of the user if an account was created"),
    ] = None
    """
    Unique identifier of the user if an account was created
    """

    user_name: typing_extensions.Annotated[
        typing.Optional[UserNameIdStr],
        FieldMetadata(alias="userName"),
        pydantic.Field(alias="userName", description="Username of the user if an account was created"),
    ] = None
    """
    Username of the user if an account was created
    """

    group_id: typing_extensions.Annotated[
        typing.Optional[PrimaryGroupId],
        FieldMetadata(alias="groupId"),
        pydantic.Field(alias="groupId", description="Primary group ID of the user if an account was created"),
    ] = None
    """
    Primary group ID of the user if an account was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
