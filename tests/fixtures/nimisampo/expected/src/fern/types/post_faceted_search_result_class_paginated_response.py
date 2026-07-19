

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PostFacetedSearchResultClassPaginatedResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Results as an array of objects
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current page
    """

    pagesize: typing.Optional[int] = pydantic.Field(default=None)
    """
    Items per page
    """

    result_class: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resultClass"),
        pydantic.Field(alias="resultClass", description="The class of the results"),
    ] = None
    """
    The class of the results
    """

    sparql_query: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sparqlQuery"),
        pydantic.Field(alias="sparqlQuery", description="The SPARQL query that was used for the results"),
    ] = None
    """
    The SPARQL query that was used for the results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
