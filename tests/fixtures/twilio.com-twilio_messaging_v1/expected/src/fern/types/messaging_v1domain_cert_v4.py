

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1DomainCertV4(UniversalBaseModel):
    cert_in_validation: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Optional JSON field describing the status and upload date of a new certificate in the process of validation
    """

    certificate_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify this Certificate resource.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date that this Domain was registered to the Twilio platform to create a new Domain object.
    """

    date_expires: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date that the private certificate associated with this domain expires. You will need to update the certificate before that date to ensure your shortened links will continue to work.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date that this Domain was last updated.
    """

    domain_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full url path for this domain.
    """

    domain_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify the Domain resource.
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
