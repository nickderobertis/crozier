

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metrics_scope import MetricsScope


class ListMetricsScopesByMonitoredProjectResponse(UniversalBaseModel):
    """
    Response for the ListMetricsScopesByMonitoredProject method.
    """

    metrics_scopes: typing_extensions.Annotated[
        typing.Optional[typing.List[MetricsScope]],
        FieldMetadata(alias="metricsScopes"),
        pydantic.Field(
            alias="metricsScopes",
            description="A set of all metrics scopes that the specified monitored project has been added to.",
        ),
    ] = None
    """
    A set of all metrics scopes that the specified monitored project has been added to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
