

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .container_info import ContainerInfo


class PrebuildTemplateInfo(UniversalBaseModel):
    container: typing.Optional[ContainerInfo] = None
    prebuild_configuration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="prebuildConfigurationId"),
        pydantic.Field(alias="prebuildConfigurationId"),
    ] = None
    template_size_in_gb: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="templateSizeInGB"), pydantic.Field(alias="templateSizeInGB")
    ] = None
    total_time_savings_in_seconds: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="totalTimeSavingsInSeconds"),
        pydantic.Field(alias="totalTimeSavingsInSeconds"),
    ] = None
    work_flow_run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workFlowRunId"), pydantic.Field(alias="workFlowRunId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
