

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServiceToken(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the service token
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of service token creation
    """

    name: str = pydantic.Field()
    """
    Name of the service token
    """

    preview_name: str
    service_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the service token
    """

    service_account_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The service account email (not routable)
    """

    service_account_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The service account name
    """

    org_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
