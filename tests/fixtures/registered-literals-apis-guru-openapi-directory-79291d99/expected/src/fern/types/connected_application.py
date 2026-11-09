

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_id import ApplicationId
from .scopes_nullable import ScopesNullable


class ConnectedApplication(UniversalBaseModel):
    """
    Describes the connected application for a particular end user.
    """

    application_id: ApplicationId
    application_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the application's website
    """

    created_at: dt.date = pydantic.Field()
    """
    The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable name of the application for display purposes
    """

    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URL that links to the application logo image.
    """

    name: str = pydantic.Field()
    """
    The name of the application
    """

    reason_for_access: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string provided by the connected app stating why they use their respective enabled products.
    """

    scopes: typing.Optional[ScopesNullable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
