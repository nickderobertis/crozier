

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class InternalQueryResponse(UniversalBaseModel):
    rows: typing.List[typing.Dict[str, typing.Any]]
    row_count: typing_extensions.Annotated[int, FieldMetadata(alias="rowCount"), pydantic.Field(alias="rowCount")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
