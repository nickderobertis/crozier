

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_status_down_details_reason import ServiceStatusDownDetailsReason


class ServiceStatusDownDetails(UniversalBaseModel):
    details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Details of the reason.
    """

    eta: typing.Optional[str] = pydantic.Field(default=None)
    """
    Estimated Time this Service could be Up again for the use.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    reason: ServiceStatusDownDetailsReason = pydantic.Field()
    """
    This field determines the reason behind status being down. Following are the possible reason for the service to be down:
    
        underMaintenance: It means that the site is under scheduled maintenance.
    
        notIntegrated: When an court with specific case type is not integrated in UniCourt.
    
        brokenIntegration: Due to some updates made to the court site our existing Integration has broken and will require a fix to be made to support this court again for a spcific case type category.
    
        sourceMigrated: When a source is migrated from one site to another for a specific case type category.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
