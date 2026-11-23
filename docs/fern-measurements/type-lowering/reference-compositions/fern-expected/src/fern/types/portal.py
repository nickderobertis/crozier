

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .portal_overrides import PortalOverrides
from .portal_settings import PortalSettings
from .portal_sources_item import PortalSourcesItem
from .portal_tallies_item import PortalTalliesItem
from .seamless_link import SeamlessLink


class Portal(UniversalBaseModel):
    id: str
    links: typing.Optional[typing.List[SeamlessLink]] = pydantic.Field(default=None)
    """
    Links written as a sole allOf of one reference.
    """

    primary_link: typing.Optional[SeamlessLink] = pydantic.Field(default=None)
    """
    A property written as a sole allOf of one reference.
    """

    votes: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Items pointing at another array component's items.
    """

    tallies: typing.Optional[typing.List[PortalTalliesItem]] = pydantic.Field(default=None)
    """
    Items pointing at a property's items.
    """

    latest_vote: typing.Optional[typing.Any] = None
    settings: typing.Optional[PortalSettings] = pydantic.Field(default=None)
    """
    A sole allOf of one reference beside an open map.
    """

    overrides: typing.Optional[PortalOverrides] = None
    sources: typing.Optional[typing.List[PortalSourcesItem]] = pydantic.Field(default=None)
    """
    Inline objects nesting the same compositions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
