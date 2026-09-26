

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RealmAuthenticationMethod(UniversalBaseModel):
    """
    Dictionary describing the properties of an authentication method for the
    organization - its enabled status and availability for use by the
    organization.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean describing whether the authentication method (i.e. its key)
    is enabled in this organization.
    """

    available: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean describing whether the authentication method is available for use.
    If false, the organization is not eligible to enable the authentication
    method.
    """

    unavailable_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason why the authentication method is unavailable. This field is optional
    and is only present when 'available' is false.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
