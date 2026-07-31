

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1ServiceUsAppToPerson(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to.
    """

    brand_registration_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string to identify the A2P brand.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Campaign Registry (TCR) Campaign ID.
    """

    campaign_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Campaign status. Examples: IN_PROGRESS, VERIFIED, FAILED.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
    """

    has_embedded_links: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicate that this SMS campaign will send messages that contain links.
    """

    has_embedded_phone: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates that this SMS campaign will send messages that contain phone numbers.
    """

    help_keywords: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    """

    help_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    """

    is_externally_registered: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the campaign was registered externally or not.
    """

    message_flow: typing.Optional[str] = pydantic.Field(default=None)
    """
    Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
    """

    message_samples: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Message samples, at least 1 and up to 5 sample messages (at least 2 for starter/sole proprietor), >=20 chars, <=1024 chars each.
    """

    messaging_service_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
    """

    mock: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean that specifies whether campaign is a mock or not. Mock campaigns will be automatically created if using a mock brand. Mock campaigns should only be used for testing purposes.
    """

    opt_in_keywords: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
    """

    opt_in_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
    """

    opt_out_keywords: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    """

    opt_out_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    """

    rate_limits: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Rate limit and/or classification set by each carrier, Ex. AT&T or T-Mobile.
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the US App to Person resource.
    """

    us_app_to_person_usecase: typing.Optional[str] = pydantic.Field(default=None)
    """
    A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING, SOLE_PROPRIETOR...]. SOLE_PROPRIETOR campaign use cases can only be created by SOLE_PROPRIETOR Brands, and there can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR Brand.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
