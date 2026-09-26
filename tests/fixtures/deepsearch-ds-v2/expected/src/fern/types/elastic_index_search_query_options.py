

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ElasticIndexSearchQueryOptions(UniversalBaseModel):
    source: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="_source"), pydantic.Field(alias="_source")
    ] = None
    from_: typing.Optional[int] = None
    size: typing.Optional[int] = None
    query: typing.Optional[typing.Dict[str, typing.Any]] = None
    aggs: typing.Optional[typing.Dict[str, typing.Any]] = None
    sort: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
