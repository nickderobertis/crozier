

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_link_button_class import CustomLinkButtonClass


class CustomLink(UniversalBaseModel):
    button_class: typing.Optional[CustomLinkButtonClass] = pydantic.Field(default=None)
    """
    The class of the first link in a group will be used for the dropdown button
    """

    content_types: typing.List[str]
    created: typing.Optional[dt.datetime] = None
    display: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    group_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Links with the same group will appear as a dropdown menu
    """

    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    link_text: str = pydantic.Field()
    """
    Jinja2 template code for link text
    """

    link_url: str = pydantic.Field()
    """
    Jinja2 template code for link URL
    """

    name: str
    new_window: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Force link to open in a new window
    """

    url: typing.Optional[str] = None
    weight: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
