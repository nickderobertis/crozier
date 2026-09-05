

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nullable_saved_function_id import NullableSavedFunctionId
from .project_settings_remote_eval_sources_item import ProjectSettingsRemoteEvalSourcesItem
from .project_settings_span_field_order_item import ProjectSettingsSpanFieldOrderItem


class ProjectSettings(UniversalBaseModel):
    comparison_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key used to join two experiments (defaults to `input`)
    """

    baseline_experiment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the experiment to use as the default baseline for comparisons
    """

    span_field_order: typing_extensions.Annotated[
        typing.Optional[typing.List[ProjectSettingsSpanFieldOrderItem]],
        FieldMetadata(alias="spanFieldOrder"),
        pydantic.Field(alias="spanFieldOrder", description="The order of the fields to display in the trace view"),
    ] = None
    """
    The order of the fields to display in the trace view
    """

    remote_eval_sources: typing.Optional[typing.List[ProjectSettingsRemoteEvalSourcesItem]] = pydantic.Field(
        default=None
    )
    """
    The remote eval sources to use for the project
    """

    disable_realtime_queries: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, disable real-time queries for this project. This can improve query performance for high-volume logs.
    """

    default_preprocessor: typing.Optional[NullableSavedFunctionId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
