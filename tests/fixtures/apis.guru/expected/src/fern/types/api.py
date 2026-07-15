

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_version import ApiVersion


class Api(UniversalBaseModel):
    """
    Meta information about API
    """

    added: dt.datetime = pydantic.Field()
    """
    Timestamp when the API was first added to the directory
    """

    preferred: str = pydantic.Field()
    """
    Recommended version
    """

    versions: typing.Dict[str, ApiVersion] = pydantic.Field()
    """
    List of supported versions of the API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
