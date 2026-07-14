

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_version_api import ServiceVersionApi
from .service_version_db import ServiceVersionDb
from .service_version_service import ServiceVersionService


class ServiceVersion(UniversalBaseModel):
    """
    Version information for a service
    """

    api: typing.Optional[ServiceVersionApi] = pydantic.Field(default=None)
    """
    Api Version string
    """

    db: typing.Optional[ServiceVersionDb] = None
    service: typing.Optional[ServiceVersionService] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
