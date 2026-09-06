

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_rendering_mode import ImageRenderingMode


class Organization(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the organization
    """

    name: str = pydantic.Field()
    """
    Name of the organization
    """

    api_url: typing.Optional[str] = None
    is_universal_api: typing.Optional[bool] = None
    is_dataplane_private: typing.Optional[bool] = None
    proxy_url: typing.Optional[str] = None
    realtime_url: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of organization creation
    """

    image_rendering_mode: typing.Optional[ImageRenderingMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
