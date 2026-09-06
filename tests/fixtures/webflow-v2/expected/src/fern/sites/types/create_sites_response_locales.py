

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_sites_response_locales_primary import CreateSitesResponseLocalesPrimary
from .create_sites_response_locales_secondary_item import CreateSitesResponseLocalesSecondaryItem


class CreateSitesResponseLocales(UniversalBaseModel):
    primary: typing.Optional[CreateSitesResponseLocalesPrimary] = pydantic.Field(default=None)
    """
    The primary locale for the site or application.
    """

    secondary: typing.Optional[typing.List[CreateSitesResponseLocalesSecondaryItem]] = pydantic.Field(default=None)
    """
    A list of secondary locales available for the site or application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
