

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logo import Logo
from .translations import Translations


class Category(UniversalBaseModel):
    count: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    id: typing.Optional[str] = None
    listing_description_text_template: typing.Optional[str] = None
    listing_features_text_template: typing.Optional[str] = None
    listing_pricing_text_template: typing.Optional[str] = None
    logo: typing.Optional[Logo] = None
    name: str
    slug: str
    translations: typing.Optional[Translations] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
