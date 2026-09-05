

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .curated_description_field import CuratedDescriptionField
from .curated_id_field import CuratedIdField
from .curated_ln_url_field import CuratedLnUrlField
from .curated_name_field import CuratedNameField
from .curated_pub_date_ms_field import CuratedPubDateMsField
from .curated_source_domain_field import CuratedSourceDomainField
from .curated_source_url_field import CuratedSourceUrlField
from .curated_total_podcasts_field import CuratedTotalPodcastsField
from .podcast_minimum import PodcastMinimum


class CuratedListSimple(UniversalBaseModel):
    description: typing.Optional[CuratedDescriptionField] = None
    id: typing.Optional[CuratedIdField] = None
    listennotes_url: typing.Optional[CuratedLnUrlField] = None
    podcasts: typing.Optional[typing.List[PodcastMinimum]] = pydantic.Field(default=None)
    """
    Minimum meta data of up to 5 podcasts in this curated list.
    """

    pub_date_ms: typing.Optional[CuratedPubDateMsField] = None
    source_domain: typing.Optional[CuratedSourceDomainField] = None
    source_url: typing.Optional[CuratedSourceUrlField] = None
    title: typing.Optional[CuratedNameField] = None
    total: typing.Optional[CuratedTotalPodcastsField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
