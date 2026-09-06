

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_sites_response_sites_item_locales_primary import ListSitesResponseSitesItemLocalesPrimary
from .list_sites_response_sites_item_locales_secondary_item import ListSitesResponseSitesItemLocalesSecondaryItem


class ListSitesResponseSitesItemLocales(UniversalBaseModel):
    primary: typing.Optional[ListSitesResponseSitesItemLocalesPrimary] = pydantic.Field(default=None)
    """
    The primary locale for the site or application.
    """

    secondary: typing.Optional[typing.List[ListSitesResponseSitesItemLocalesSecondaryItem]] = pydantic.Field(
        default=None
    )
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
