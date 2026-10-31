

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Report(UniversalBaseModel):
    """
    The report object
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of this account
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the campaign
    """

    sent: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of emails sent
    """

    accepted: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of emails accepted by the recipient mail servers
    """

    cleaned: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of deleted subscribers
    """

    complained: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of spam complaints (by clicking on the spam button in the email program)
    """

    hardbounced: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of hard-bounces
    """

    unsubscribed: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of unsubscriptions
    """

    opened_unique: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of subscribers who have opened the email once or more
    """

    clicked_unique: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of subscribers who have clicked on the email once or more
    """

    webversion_unique: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of subscribers who have requested the web version
    """

    accepted_ratio: typing.Optional[float] = pydantic.Field(default=None)
    """
    The ratio of accepted emails to the number of sent emails
    """

    opened_ratio: typing.Optional[float] = pydantic.Field(default=None)
    """
    The ratio of emails opened once or more to the number of accepted emails
    """

    clicked_ratio: typing.Optional[float] = pydantic.Field(default=None)
    """
    The ratio of emails that have been clicked once or more to the number of accepted emails
    """

    from_automation: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this delivery came from an automation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
