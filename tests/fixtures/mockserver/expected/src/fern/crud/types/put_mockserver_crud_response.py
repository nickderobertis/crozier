

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverCrudResponse(UniversalBaseModel):
    base_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="basePath"), pydantic.Field(alias="basePath")
    ] = None
    id_strategy: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idStrategy"), pydantic.Field(alias="idStrategy")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
