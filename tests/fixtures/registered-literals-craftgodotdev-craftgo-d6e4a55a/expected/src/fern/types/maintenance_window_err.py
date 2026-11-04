

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .maintenance_reason import MaintenanceReason


class MaintenanceWindowErr(UniversalBaseModel):
    """
    ServiceUnavailable error response (HTTP 503).
    """

    estimated_end_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="estimatedEndAt"), pydantic.Field(alias="estimatedEndAt")
    ]
    reason: MaintenanceReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
