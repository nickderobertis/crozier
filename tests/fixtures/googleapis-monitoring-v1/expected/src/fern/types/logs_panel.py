

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LogsPanel(UniversalBaseModel):
    """
    A widget that displays a stream of log.
    """

    filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    A filter that chooses which log entries to return. See Advanced Logs Queries (https://cloud.google.com/logging/docs/view/advanced-queries). Only log entries that match the filter are returned. An empty filter matches all log entries.
    """

    resource_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="resourceNames"),
        pydantic.Field(
            alias="resourceNames",
            description="The names of logging resources to collect logs for. Currently only projects are supported. If empty, the widget will default to the host project.",
        ),
    ] = None
    """
    The names of logging resources to collect logs for. Currently only projects are supported. If empty, the widget will default to the host project.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
