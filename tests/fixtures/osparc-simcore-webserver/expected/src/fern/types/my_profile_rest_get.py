

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .aggregated_preferences import AggregatedPreferences
from .first_name_str import FirstNameStr
from .last_name_str import LastNameStr
from .lower_case_email_str import LowerCaseEmailStr
from .my_groups_get import MyGroupsGet
from .my_profile_address_get import MyProfileAddressGet
from .my_profile_privacy_get import MyProfilePrivacyGet
from .my_profile_rest_get_role import MyProfileRestGetRole
from .supported_locale import SupportedLocale
from .user_id_int import UserIdInt


class MyProfileRestGet(UniversalBaseModel):
    id: UserIdInt
    user_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="userName"), pydantic.Field(alias="userName", description="Unique username identifier")
    ]
    """
    Unique username identifier
    """

    first_name: typing.Optional[FirstNameStr] = None
    last_name: typing.Optional[LastNameStr] = None
    login: LowerCaseEmailStr
    phone: typing.Optional[str] = None
    language: typing.Optional[SupportedLocale] = pydantic.Field(default=None)
    """
    Persisted UI/communications language. None means no persisted choice.
    """

    role: MyProfileRestGetRole
    groups: typing.Optional[MyGroupsGet] = None
    gravatar_id: typing.Optional[str] = None
    expiration_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="expirationDate"),
        pydantic.Field(
            alias="expirationDate",
            description="If user has a trial account, it sets the expiration date, otherwise None",
        ),
    ] = None
    """
    If user has a trial account, it sets the expiration date, otherwise None
    """

    privacy: MyProfilePrivacyGet
    preferences: AggregatedPreferences
    contact: typing.Optional[MyProfileAddressGet] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
