

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .amount import Amount
from .avatar import Avatar
from .billing_contract_subscription import BillingContractSubscription
from .customer import Customer
from .customer_limit import CustomerLimit
from .label_user import LabelUser
from .notification_filter import NotificationFilter
from .pointer import Pointer
from .relation_user import RelationUser
from .tax_resident import TaxResident
from .ubo import Ubo


class UserCompanyRead(UniversalBaseModel):
    address_main: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The company's main address.
    """

    address_postal: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The company's postal address.
    """

    alias: typing.Optional[typing.List[Pointer]] = pydantic.Field(default=None)
    """
    The aliases of the account.
    """

    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The company's avatar.
    """

    billing_contract: typing.Optional[typing.List[BillingContractSubscription]] = pydantic.Field(default=None)
    """
    The subscription of the company.
    """

    chamber_of_commerce_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's chamber of commerce number.
    """

    counter_bank_iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's other bank account IBAN, through which we verify it.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country as an ISO 3166-1 alpha-2 country code.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the company object's creation.
    """

    customer: typing.Optional[Customer] = pydantic.Field(default=None)
    """
    The customer profile of the company.
    """

    customer_limit: typing.Optional[CustomerLimit] = pydantic.Field(default=None)
    """
    The customer limits of the company.
    """

    daily_limit_without_confirmation_login: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount the company can pay in the session without asking for credentials.
    """

    deny_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user deny reason.
    """

    directors: typing.Optional[typing.List[LabelUser]] = pydantic.Field(default=None)
    """
    The existing bunq aliases for the company's directors.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's display name.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the modified company.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    """

    legal_form: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's legal form.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company name.
    """

    notification_filters: typing.Optional[typing.List[NotificationFilter]] = pydantic.Field(default=None)
    """
    The types of notifications that will result in a push notification or URL callback for this UserCompany.
    """

    public_nick_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's public nick name.
    """

    public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's public UUID.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    """

    relations: typing.Optional[typing.List[RelationUser]] = pydantic.Field(default=None)
    """
    The relations for this user.
    """

    sector_of_industry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sector of industry.
    """

    session_timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    The setting for the session timeout of the company in seconds.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user status. Can be: ACTIVE, SIGNUP, RECOVERY.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.
    """

    tax_resident: typing.Optional[typing.List[TaxResident]] = pydantic.Field(default=None)
    """
    The user's tax residence numbers for different countries.
    """

    type_of_business_entity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of business entity.
    """

    ubo: typing.Optional[typing.List[Ubo]] = pydantic.Field(default=None)
    """
    The names of the company's ultimate beneficiary owners. Minimum zero, maximum four.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the company object's last update.
    """

    version_terms_of_service: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the terms of service accepted by the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
