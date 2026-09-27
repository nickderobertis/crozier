

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverCassettesResponse(UniversalBaseModel):
    path: typing.Optional[str] = None
    filename: typing.Optional[str] = None
    expectation_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="expectationCount"), pydantic.Field(alias="expectationCount")
    ] = None
    origin: typing.Optional[str] = None
    last_used: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lastUsed"), pydantic.Field(alias="lastUsed")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
