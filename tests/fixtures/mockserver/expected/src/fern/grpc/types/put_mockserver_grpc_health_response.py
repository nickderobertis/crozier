

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverGrpcHealthResponse(UniversalBaseModel):
    status: typing.Optional[str] = None
    service: typing.Optional[str] = None
    serving_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="servingStatus"), pydantic.Field(alias="servingStatus")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
