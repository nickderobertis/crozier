

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .curated_id_field import CuratedIdField
from .curated_ln_url_field import CuratedLnUrlField
from .curated_pub_date_ms_field import CuratedPubDateMsField
from .curated_source_domain_field import CuratedSourceDomainField
from .curated_source_url_field import CuratedSourceUrlField
from .curated_total_podcasts_field import CuratedTotalPodcastsField
from .podcast_minimum import PodcastMinimum


class CuratedListSearchResult(UniversalBaseModel):
    """
    When **type** is *curated*.
    """

    description_highlighted: typing.Optional[str] = pydantic.Field(default=None)
    """
    Highlighted segment of this curated list's description
    """

    description_original: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plain text of this curated list's description
    """

    id: typing.Optional[CuratedIdField] = None
    listennotes_url: typing.Optional[CuratedLnUrlField] = None
    podcasts: typing.Optional[typing.List[PodcastMinimum]] = pydantic.Field(default=None)
    """
    Up to 5 podcasts in this curated list.
    """

    pub_date_ms: typing.Optional[CuratedPubDateMsField] = None
    source_domain: typing.Optional[CuratedSourceDomainField] = None
    source_url: typing.Optional[CuratedSourceUrlField] = None
    title_highlighted: typing.Optional[str] = pydantic.Field(default=None)
    """
    Highlighted segment of this curated list's title
    """

    title_original: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plain text of this curated list's title
    """

    total: typing.Optional[CuratedTotalPodcastsField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
