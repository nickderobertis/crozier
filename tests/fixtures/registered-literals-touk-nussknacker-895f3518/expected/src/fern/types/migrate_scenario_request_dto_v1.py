

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MigrateScenarioRequestDtoV1(UniversalBaseModel):
    version: int
    source_environment_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceEnvironmentId"), pydantic.Field(alias="sourceEnvironmentId")
    ]
    remote_user_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="remoteUserName"), pydantic.Field(alias="remoteUserName")
    ]
    processing_mode: typing_extensions.Annotated[
        str, FieldMetadata(alias="processingMode"), pydantic.Field(alias="processingMode")
    ]
    engine_setup_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="engineSetupName"), pydantic.Field(alias="engineSetupName")
    ]
    process_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="processCategory"), pydantic.Field(alias="processCategory")
    ]
    scenario_graph: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="scenarioGraph"), pydantic.Field(alias="scenarioGraph")
    ]
    process_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="processName"), pydantic.Field(alias="processName")
    ]
    is_fragment: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isFragment"), pydantic.Field(alias="isFragment")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
