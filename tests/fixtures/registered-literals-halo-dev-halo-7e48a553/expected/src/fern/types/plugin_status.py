

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition import Condition
from .plugin_status_last_probe_state import PluginStatusLastProbeState
from .plugin_status_phase import PluginStatusPhase


class PluginStatus(UniversalBaseModel):
    """
    Observed plugin lifecycle and runtime asset state.
    """

    conditions: typing.Optional[typing.List[Condition]] = pydantic.Field(default=None)
    """
    Reconciliation conditions for the plugin.
    """

    entry: typing.Optional[str] = pydantic.Field(default=None)
    """
    JavaScript bundle entry path served for the plugin UI.
    """

    last_probe_state: typing_extensions.Annotated[
        typing.Optional[PluginStatusLastProbeState],
        FieldMetadata(alias="lastProbeState"),
        pydantic.Field(alias="lastProbeState", description="Last PF4J probe state observed for the plugin."),
    ] = None
    """
    Last PF4J probe state observed for the plugin.
    """

    last_start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastStartTime"),
        pydantic.Field(alias="lastStartTime", description="Last time the plugin started successfully."),
    ] = None
    """
    Last time the plugin started successfully.
    """

    load_location: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="loadLocation"),
        pydantic.Field(alias="loadLocation", description="URI location where the plugin artifact was loaded from."),
    ] = None
    """
    URI location where the plugin artifact was loaded from.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resolved logo URL or attachment URI for the plugin.
    """

    phase: typing.Optional[PluginStatusPhase] = pydantic.Field(default=None)
    """
    Current plugin lifecycle phase.
    """

    stylesheet: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stylesheet bundle path served for the plugin UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
