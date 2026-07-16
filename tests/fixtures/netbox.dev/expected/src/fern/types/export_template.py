

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExportTemplate(UniversalBaseModel):
    as_attachment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Download file as attachment
    """

    content_types: typing.List[str]
    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    file_extension: typing.Optional[str] = pydantic.Field(default=None)
    """
    Extension to append to the rendered filename
    """

    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    mime_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Defaults to <code>text/plain</code>
    """

    name: str
    template_code: str = pydantic.Field()
    """
    Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
