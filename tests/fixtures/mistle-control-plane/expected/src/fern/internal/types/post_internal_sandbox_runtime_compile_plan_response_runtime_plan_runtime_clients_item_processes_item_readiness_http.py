

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemReadinessHttp(
    UniversalBaseModel
):
    url: str
    expected_status: typing_extensions.Annotated[
        int, FieldMetadata(alias="expectedStatus"), pydantic.Field(alias="expectedStatus")
    ]
    timeout_ms: typing_extensions.Annotated[int, FieldMetadata(alias="timeoutMs"), pydantic.Field(alias="timeoutMs")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
