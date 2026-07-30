

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinationGoogleSheetsConfig(UniversalBaseModel):
    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Google OAuth2 client ID (env: GOOGLE_CLIENT_ID)
    """

    client_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Google OAuth2 client secret (env: GOOGLE_CLIENT_SECRET)
    """

    access_token: typing.Optional[str] = None
    refresh_token: str = pydantic.Field()
    """
    OAuth2 refresh token
    """

    spreadsheet_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Target spreadsheet ID (created if omitted)
    """

    spreadsheet_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title when creating a new spreadsheet
    """

    batch_size: typing.Optional[float] = pydantic.Field(default=None)
    """
    Rows per Sheets API append call
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
