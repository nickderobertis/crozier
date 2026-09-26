

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .monitored_project import MonitoredProject


class MetricsScope(UniversalBaseModel):
    """
    Represents a Metrics Scope (https://cloud.google.com/monitoring/settings#concept-scope) in Cloud Monitoring, which specifies one or more Google projects and zero or more AWS accounts to monitor together.
    """

    create_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createTime"),
        pydantic.Field(alias="createTime", description="Output only. The time when this Metrics Scope was created."),
    ] = None
    """
    Output only. The time when this Metrics Scope was created.
    """

    monitored_projects: typing_extensions.Annotated[
        typing.Optional[typing.List[MonitoredProject]],
        FieldMetadata(alias="monitoredProjects"),
        pydantic.Field(
            alias="monitoredProjects", description="Output only. The list of projects monitored by this Metrics Scope."
        ),
    ] = None
    """
    Output only. The list of projects monitored by this Metrics Scope.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Immutable. The resource name of the Monitoring Metrics Scope. On input, the resource name can be specified with the scoping project ID or number. On output, the resource name is specified with the scoping project number. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}
    """

    update_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updateTime"),
        pydantic.Field(
            alias="updateTime", description="Output only. The time when this Metrics Scope record was last updated."
        ),
    ] = None
    """
    Output only. The time when this Metrics Scope record was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
