

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .compatibility import Compatibility


class ServiceRelease(UniversalBaseModel):
    version: str
    version_display: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="versionDisplay"),
        pydantic.Field(alias="versionDisplay", description="If None, then display `version`"),
    ] = None
    """
    If None, then display `version`
    """

    released: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When provided, it indicates the release timestamp
    """

    retired: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    whether this service is planned to be retired. If None, the service is still active. If now<retired then the service is deprecated. If retired<now then the service is retired and should not be used.
    """

    compatibility: typing.Optional[Compatibility] = pydantic.Field(default=None)
    """
    Compatibility with other releases at this moment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
