

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message import Message
from .query_hal_links import QueryHalLinks
from .query_output import QueryOutput


class QueryResponse(UniversalBaseModel):
    """
    Represents a single named query.
    """

    links: typing_extensions.Annotated[QueryHalLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    attrs: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    System provided metadata for the query definition.
    """

    name: str = pydantic.Field()
    """
    Name of the stored query definition.
    """

    meta: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User metadata for the query definition.
    """

    query: QueryOutput
    messages: typing.Optional[typing.List[Message]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
