

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_project_automation_config_batch_size_credentials import PatchProjectAutomationConfigBatchSizeCredentials
from .patch_project_automation_config_batch_size_event_type import PatchProjectAutomationConfigBatchSizeEventType
from .patch_project_automation_config_batch_size_export_definition import (
    PatchProjectAutomationConfigBatchSizeExportDefinition,
)
from .patch_project_automation_config_batch_size_format import PatchProjectAutomationConfigBatchSizeFormat


class PatchProjectAutomationConfigBatchSize(UniversalBaseModel):
    event_type: PatchProjectAutomationConfigBatchSizeEventType = pydantic.Field()
    """
    The type of automation.
    """

    export_definition: PatchProjectAutomationConfigBatchSizeExportDefinition = pydantic.Field()
    """
    The definition of what to export
    """

    export_path: str = pydantic.Field()
    """
    The path to export the results to. It should include the storage protocol and prefix, e.g. s3://bucket-name/path/to/export
    """

    format: PatchProjectAutomationConfigBatchSizeFormat = pydantic.Field()
    """
    The format to export the results in
    """

    interval_seconds: float = pydantic.Field()
    """
    Perform the triggered action at most once in this interval of seconds
    """

    credentials: PatchProjectAutomationConfigBatchSizeCredentials
    batch_size: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of rows to export in each batch
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
