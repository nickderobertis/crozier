

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tollfree_verification_enum_opt_in_type import TollfreeVerificationEnumOptInType
from .tollfree_verification_enum_status import TollfreeVerificationEnumStatus


class MessagingV1TollfreeVerification(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Tollfree Verification resource.
    """

    additional_information: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional information to be provided for verification.
    """

    business_city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city of the business or organization using the Tollfree number.
    """

    business_contact_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address of the contact for the business or organization using the Tollfree number.
    """

    business_contact_first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first name of the contact for the business or organization using the Tollfree number.
    """

    business_contact_last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last name of the contact for the business or organization using the Tollfree number.
    """

    business_contact_phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number of the contact for the business or organization using the Tollfree number.
    """

    business_country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the business or organization using the Tollfree number.
    """

    business_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the business or organization using the Tollfree number.
    """

    business_postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code of the business or organization using the Tollfree number.
    """

    business_state_province_region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state/province/region of the business or organization using the Tollfree number.
    """

    business_street_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The address of the business or organization using the Tollfree number.
    """

    business_street_address2: typing.Optional[str] = pydantic.Field(default=None)
    """
    The address of the business or organization using the Tollfree number.
    """

    business_website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website of the business or organization using the Tollfree number.
    """

    customer_profile_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Customer's Profile Bundle BundleSid.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    error_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    The error code given when a Tollfree Verification has been rejected.
    """

    external_reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional external reference ID supplied by customer and echoed back on status retrieval.
    """

    message_volume: typing.Optional[str] = pydantic.Field(default=None)
    """
    Estimate monthly volume of messages from the Tollfree Number.
    """

    notification_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address to receive the notification about the verification result. .
    """

    opt_in_image_urls: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.
    """

    opt_in_type: typing.Optional[TollfreeVerificationEnumOptInType] = pydantic.Field(default=None)
    """
    Describe how a user opts-in to text messages.
    """

    production_message_sample: typing.Optional[str] = pydantic.Field(default=None)
    """
    An example of message content, i.e. a sample message.
    """

    regulated_item_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the Regulated Item.
    """

    rejection_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rejection reason given when a Tollfree Verification has been rejected.
    """

    resource_links: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The URLs of the documents associated with the Tollfree Verification resource.
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string to identify Tollfree Verification.
    """

    status: typing.Optional[TollfreeVerificationEnumStatus] = pydantic.Field(default=None)
    """
    The compliance status of the Tollfree Verification record.
    """

    tollfree_phone_number_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the Phone Number associated with the Tollfree Verification.
    """

    trust_product_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tollfree TrustProduct Bundle BundleSid.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the Tollfree Verification resource.
    """

    use_case_categories: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The category of the use case for the Tollfree Number. List as many are applicable..
    """

    use_case_summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    Use this to further explain how messaging is used by the business or organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
