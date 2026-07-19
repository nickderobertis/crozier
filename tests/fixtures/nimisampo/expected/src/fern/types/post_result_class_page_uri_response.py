

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PostResultClassPageUriResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    An array containing one object describing the resource
    """

    sparql_query: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sparqlQuery"),
        pydantic.Field(alias="sparqlQuery", description="The SPARQL query that was used for retrieving the metadata"),
    ] = None
    """
    The SPARQL query that was used for retrieving the metadata
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
