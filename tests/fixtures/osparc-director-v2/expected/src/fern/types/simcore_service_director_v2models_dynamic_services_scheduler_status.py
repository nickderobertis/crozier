

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dynamic_sidecar_status import DynamicSidecarStatus


class SimcoreServiceDirectorV2ModelsDynamicServicesSchedulerStatus(UniversalBaseModel):
    """
    Generated from data from docker container inspect API
    """

    current: DynamicSidecarStatus = pydantic.Field()
    """
    status of the service
    """

    info: str = pydantic.Field()
    """
    additional information for the user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
