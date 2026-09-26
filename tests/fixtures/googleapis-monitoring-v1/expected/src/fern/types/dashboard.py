

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_layout import ColumnLayout
from .dashboard_filter import DashboardFilter
from .grid_layout import GridLayout
from .mosaic_layout import MosaicLayout
from .row_layout import RowLayout


class Dashboard(UniversalBaseModel):
    """
    A Google Stackdriver dashboard. Dashboards define the content and layout of pages in the Stackdriver web application.
    """

    column_layout: typing_extensions.Annotated[
        typing.Optional[ColumnLayout],
        FieldMetadata(alias="columnLayout"),
        pydantic.Field(
            alias="columnLayout",
            description="The content is divided into equally spaced columns and the widgets are arranged vertically.",
        ),
    ] = None
    """
    The content is divided into equally spaced columns and the widgets are arranged vertically.
    """

    dashboard_filters: typing_extensions.Annotated[
        typing.Optional[typing.List[DashboardFilter]],
        FieldMetadata(alias="dashboardFilters"),
        pydantic.Field(
            alias="dashboardFilters",
            description="Filters to reduce the amount of data charted based on the filter criteria.",
        ),
    ] = None
    """
    Filters to reduce the amount of data charted based on the filter criteria.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Required. The mutable, human-readable name."),
    ] = None
    """
    Required. The mutable, human-readable name.
    """

    etag: typing.Optional[str] = pydantic.Field(default=None)
    """
    etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An etag is returned in the response to GetDashboard, and users are expected to put that etag in the request to UpdateDashboard to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.
    """

    grid_layout: typing_extensions.Annotated[
        typing.Optional[GridLayout],
        FieldMetadata(alias="gridLayout"),
        pydantic.Field(
            alias="gridLayout",
            description="Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.",
        ),
    ] = None
    """
    Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Labels applied to the dashboard
    """

    mosaic_layout: typing_extensions.Annotated[
        typing.Optional[MosaicLayout],
        FieldMetadata(alias="mosaicLayout"),
        pydantic.Field(
            alias="mosaicLayout",
            description="The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.",
        ),
    ] = None
    """
    The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier. The resource name of the dashboard.
    """

    row_layout: typing_extensions.Annotated[
        typing.Optional[RowLayout],
        FieldMetadata(alias="rowLayout"),
        pydantic.Field(
            alias="rowLayout",
            description="The content is divided into equally spaced rows and the widgets are arranged horizontally.",
        ),
    ] = None
    """
    The content is divided into equally spaced rows and the widgets are arranged horizontally.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
