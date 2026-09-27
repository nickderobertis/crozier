

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MonitoredProject(UniversalBaseModel):
    """
    A project being monitored (https://cloud.google.com/monitoring/settings/multiple-projects#create-multi) by a Metrics Scope.
    """

    create_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createTime"),
        pydantic.Field(alias="createTime", description="Output only. The time when this MonitoredProject was created."),
    ] = None
    """
    Output only. The time when this MonitoredProject was created.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Immutable. The resource name of the MonitoredProject. On input, the resource name includes the scoping project ID and monitored project ID. On output, it contains the equivalent project numbers. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
