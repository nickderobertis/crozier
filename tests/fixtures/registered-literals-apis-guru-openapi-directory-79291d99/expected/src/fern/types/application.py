

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_id import ApplicationId


class Application(UniversalBaseModel):
    """
    Metadata about the application
    """

    application_id: ApplicationId
    application_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the application's website
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the city of the client’s headquarters.
    """

    company_legal_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the name of client’s legal entity.
    """

    country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the country code of the client’s headquarters.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable name of the application for display purposes
    """

    join_date: dt.date = pydantic.Field()
    """
    The date this application was granted production access at Plaid in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC.
    """

    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URL that links to the application logo image.
    """

    name: str = pydantic.Field()
    """
    The name of the application
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the postal code of the client’s headquarters.
    """

    reason_for_access: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string provided by the connected app stating why they use their respective enabled products.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing the region of the client’s headquarters.
    """

    use_case: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string representing client’s broad use case as assessed by Plaid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
