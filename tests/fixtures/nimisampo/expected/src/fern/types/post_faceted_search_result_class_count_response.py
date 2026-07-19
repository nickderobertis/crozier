

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PostFacetedSearchResultClassCountResponse(UniversalBaseModel):
    data: typing.Optional[str] = None
    sparql_query: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sparqlQuery"), pydantic.Field(alias="sparqlQuery")
    ] = None
    result_class: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resultClass"), pydantic.Field(alias="resultClass")
    ] = None
    constraints: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
