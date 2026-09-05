

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_automation_config_btql_export_credentials import ProjectAutomationConfigBtqlExportCredentials
from .project_automation_config_btql_export_export_definition import ProjectAutomationConfigBtqlExportExportDefinition
from .project_automation_config_btql_export_format import ProjectAutomationConfigBtqlExportFormat


class ProjectAutomationConfigBtqlExport(UniversalBaseModel):
    export_definition: ProjectAutomationConfigBtqlExportExportDefinition = pydantic.Field()
    """
    The definition of what to export
    """

    export_path: str = pydantic.Field()
    """
    The path to export the results to. It should include the storage protocol and prefix, e.g. s3://bucket-name/path/to/export
    """

    format: ProjectAutomationConfigBtqlExportFormat = pydantic.Field()
    """
    The format to export the results in
    """

    interval_seconds: float = pydantic.Field()
    """
    Perform the triggered action at most once in this interval of seconds
    """

    credentials: ProjectAutomationConfigBtqlExportCredentials
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
