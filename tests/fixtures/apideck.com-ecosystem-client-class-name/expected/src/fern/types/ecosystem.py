

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card_settings import CardSettings
from .cta_settings import CtaSettings
from .custom_settings import CustomSettings
from .ecosystem_menu_position import EcosystemMenuPosition
from .ecosystem_menu_style import EcosystemMenuStyle
from .ecosystem_navigation_mobile_menu_type import EcosystemNavigationMobileMenuType
from .integration_settings import IntegrationSettings
from .lead_form_settings import LeadFormSettings
from .listing_settings import ListingSettings
from .masthead_settings import MastheadSettings
from .meta_tag_settings import MetaTagSettings


class Ecosystem(UniversalBaseModel):
    about: typing.Optional[str] = None
    alternatives_background_color: typing.Optional[str] = None
    alternatives_color: typing.Optional[str] = None
    attribution: typing.Optional[bool] = None
    body_background_color: typing.Optional[str] = None
    body_button_background_color: typing.Optional[str] = None
    body_button_color: typing.Optional[str] = None
    body_color: typing.Optional[str] = None
    body_link_color: typing.Optional[str] = None
    card_settings: typing.Optional[CardSettings] = None
    categories_count_badge: typing.Optional[bool] = None
    categories_show_max_items: typing.Optional[int] = None
    collections_count_badge: typing.Optional[bool] = None
    collections_title: typing.Optional[str] = None
    create_link: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    cta_settings: typing.Optional[CtaSettings] = None
    custom_domain: typing.Optional[str] = None
    custom_settings: typing.Optional[CustomSettings] = None
    detail_pages_enabled: typing.Optional[bool] = None
    footer_background_color: typing.Optional[str] = None
    footer_color: typing.Optional[str] = None
    google_site_verification_id: typing.Optional[str] = None
    hide_install_buttons: typing.Optional[bool] = None
    home_page_collection_category_cards: typing.Optional[bool] = None
    home_page_show_all_listings: typing.Optional[bool] = None
    id: typing.Optional[str] = None
    installation_request_flow_enabled: typing.Optional[bool] = None
    integration_settings: typing.Optional[IntegrationSettings] = None
    is_published: bool
    lead_form_settings: typing.Optional[LeadFormSettings] = None
    listing_settings: typing.Optional[ListingSettings] = None
    masthead_settings: typing.Optional[MastheadSettings] = None
    menu_position: typing.Optional[EcosystemMenuPosition] = None
    menu_style: typing.Optional[EcosystemMenuStyle] = None
    meta_tag_settings: typing.Optional[MetaTagSettings] = None
    name: str
    navigation_background_color: typing.Optional[str] = None
    navigation_color: typing.Optional[str] = None
    navigation_logo_post_fix: typing.Optional[str] = None
    navigation_mobile_menu_type: typing.Optional[EcosystemNavigationMobileMenuType] = None
    navigation_sticky: typing.Optional[bool] = None
    primary_color: typing.Optional[str] = None
    privacy_link: typing.Optional[str] = None
    request_link: typing.Optional[str] = None
    shadow_page_description: typing.Optional[str] = None
    shadow_pages_enabled: typing.Optional[bool] = None
    show_attribution_badge: typing.Optional[bool] = None
    show_requested_listings: typing.Optional[bool] = None
    slug: str
    terms_link: typing.Optional[str] = None
    total_published_listings: typing.Optional[int] = None
    unify_application_id: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None
    utm_campaign: typing.Optional[str] = None
    website: typing.Optional[str] = None
    zaps_menu_title: typing.Optional[str] = None
    zaps_page_enabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
