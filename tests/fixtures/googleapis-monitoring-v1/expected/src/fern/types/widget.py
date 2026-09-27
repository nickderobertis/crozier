

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_chart import AlertChart
from .collapsible_group import CollapsibleGroup
from .empty import Empty
from .error_reporting_panel import ErrorReportingPanel
from .incident_list import IncidentList
from .logs_panel import LogsPanel
from .pie_chart import PieChart
from .scorecard import Scorecard
from .section_header import SectionHeader
from .single_view_group import SingleViewGroup
from .text import Text
from .time_series_table import TimeSeriesTable
from .xy_chart import XyChart


class Widget(UniversalBaseModel):
    """
    Widget contains a single dashboard component and configuration of how to present the component in the dashboard.
    """

    alert_chart: typing_extensions.Annotated[
        typing.Optional[AlertChart],
        FieldMetadata(alias="alertChart"),
        pydantic.Field(alias="alertChart", description="A chart of alert policy data."),
    ] = None
    """
    A chart of alert policy data.
    """

    blank: typing.Optional[Empty] = pydantic.Field(default=None)
    """
    A blank space.
    """

    collapsible_group: typing_extensions.Annotated[
        typing.Optional[CollapsibleGroup],
        FieldMetadata(alias="collapsibleGroup"),
        pydantic.Field(
            alias="collapsibleGroup",
            description="A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.",
        ),
    ] = None
    """
    A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.
    """

    error_reporting_panel: typing_extensions.Annotated[
        typing.Optional[ErrorReportingPanel],
        FieldMetadata(alias="errorReportingPanel"),
        pydantic.Field(alias="errorReportingPanel", description="A widget that displays a list of error groups."),
    ] = None
    """
    A widget that displays a list of error groups.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional. The widget id. Ids may be made up of alphanumerics, dashes and underscores. Widget ids are optional.
    """

    incident_list: typing_extensions.Annotated[
        typing.Optional[IncidentList],
        FieldMetadata(alias="incidentList"),
        pydantic.Field(alias="incidentList", description="A widget that shows list of incidents."),
    ] = None
    """
    A widget that shows list of incidents.
    """

    logs_panel: typing_extensions.Annotated[
        typing.Optional[LogsPanel],
        FieldMetadata(alias="logsPanel"),
        pydantic.Field(alias="logsPanel", description="A widget that shows a stream of logs."),
    ] = None
    """
    A widget that shows a stream of logs.
    """

    pie_chart: typing_extensions.Annotated[
        typing.Optional[PieChart],
        FieldMetadata(alias="pieChart"),
        pydantic.Field(alias="pieChart", description="A widget that displays timeseries data as a pie chart."),
    ] = None
    """
    A widget that displays timeseries data as a pie chart.
    """

    scorecard: typing.Optional[Scorecard] = pydantic.Field(default=None)
    """
    A scorecard summarizing time series data.
    """

    section_header: typing_extensions.Annotated[
        typing.Optional[SectionHeader],
        FieldMetadata(alias="sectionHeader"),
        pydantic.Field(
            alias="sectionHeader",
            description="A widget that defines a section header for easier navigation of the dashboard.",
        ),
    ] = None
    """
    A widget that defines a section header for easier navigation of the dashboard.
    """

    single_view_group: typing_extensions.Annotated[
        typing.Optional[SingleViewGroup],
        FieldMetadata(alias="singleViewGroup"),
        pydantic.Field(
            alias="singleViewGroup", description="A widget that groups the other widgets by using a dropdown menu."
        ),
    ] = None
    """
    A widget that groups the other widgets by using a dropdown menu.
    """

    text: typing.Optional[Text] = pydantic.Field(default=None)
    """
    A raw string or markdown displaying textual content.
    """

    time_series_table: typing_extensions.Annotated[
        typing.Optional[TimeSeriesTable],
        FieldMetadata(alias="timeSeriesTable"),
        pydantic.Field(
            alias="timeSeriesTable", description="A widget that displays time series data in a tabular format."
        ),
    ] = None
    """
    A widget that displays time series data in a tabular format.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional. The title of the widget.
    """

    xy_chart: typing_extensions.Annotated[
        typing.Optional[XyChart],
        FieldMetadata(alias="xyChart"),
        pydantic.Field(alias="xyChart", description="A chart of time series data."),
    ] = None
    """
    A chart of time series data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
