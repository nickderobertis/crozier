

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class WorkspaceGetServiceCountResponse(UniversalBaseModel):
    website: float
    application: float
    monitor: float
    server: float
    telemetry: float
    page: float
    survey: float
    feed: float
    short_link: typing_extensions.Annotated[float, FieldMetadata(alias="shortLink"), pydantic.Field(alias="shortLink")]
    ai_gateway: typing_extensions.Annotated[float, FieldMetadata(alias="aiGateway"), pydantic.Field(alias="aiGateway")]
    function_worker: typing_extensions.Annotated[
        float, FieldMetadata(alias="functionWorker"), pydantic.Field(alias="functionWorker")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
