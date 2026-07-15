

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .category import Category
from .collection import Collection
from .file import File
from .logo import Logo
from .media import Media
from .partner import Partner
from .product import Product
from .screenshot import Screenshot
from .translations import Translations


class Listing(UniversalBaseModel):
    automate_id: typing.Optional[str] = None
    blendr_id: typing.Optional[str] = None
    card_background_color: typing.Optional[str] = None
    card_background_image: typing.Optional[File] = None
    categories: typing.Optional[typing.List[Category]] = None
    cloud_service_id: typing.Optional[str] = None
    collections: typing.Optional[typing.List[Collection]] = None
    combidesk_id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    detail_page_disabled: typing.Optional[bool] = None
    external_id: typing.Optional[str] = None
    features: typing.Optional[str] = None
    id: typing.Optional[str] = None
    integromat_id: typing.Optional[str] = None
    logo: typing.Optional[Logo] = None
    media: typing.Optional[typing.List[Media]] = None
    meta_tag_description: typing.Optional[str] = None
    meta_tag_keywords: typing.Optional[str] = None
    meta_tag_title: typing.Optional[str] = None
    microsoft_flow_id: typing.Optional[str] = None
    name: str
    native_integration: typing.Optional[bool] = None
    native_integration_link: typing.Optional[str] = None
    partner: typing.Optional[Partner] = None
    piesync_id: typing.Optional[str] = None
    pricing: typing.Optional[str] = None
    products: typing.Optional[typing.List[Product]] = None
    published: typing.Optional[bool] = None
    published_at: typing.Optional[dt.datetime] = None
    screenshots: typing.Optional[typing.List[Screenshot]] = None
    segment_id: typing.Optional[str] = None
    slug: str
    sticky: typing.Optional[bool] = None
    tag_line: typing.Optional[str] = None
    third_party_integration: typing.Optional[bool] = None
    third_party_integration_link: typing.Optional[str] = None
    translations: typing.Optional[Translations] = None
    tray_io_id: typing.Optional[str] = None
    unify_connector_id: typing.Optional[str] = None
    upcoming: typing.Optional[bool] = None
    updated_at: typing.Optional[dt.datetime] = None
    zapier_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
