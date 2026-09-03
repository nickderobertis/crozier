

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_status_services_database import HealthStatusServicesDatabase
from .health_status_services_external_apis import HealthStatusServicesExternalApis


class HealthStatusServices(UniversalBaseModel):
    database: typing.Optional[HealthStatusServicesDatabase] = None
    external_apis: typing.Optional[HealthStatusServicesExternalApis] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
