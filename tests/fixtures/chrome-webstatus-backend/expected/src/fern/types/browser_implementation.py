

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .browser_implementation_status import BrowserImplementationStatus


class BrowserImplementation(UniversalBaseModel):
    status: typing.Optional[BrowserImplementationStatus] = None
    date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the feature was implemented in a browser. (RFC 3339, section 5.6, for example, 2017-07-21)
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The browser version in which the feature became available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
