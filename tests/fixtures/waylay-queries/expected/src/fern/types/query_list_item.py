

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_hal_links import QueryHalLinks


class QueryListItem(UniversalBaseModel):
    """
    Listing of a query definition item.
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
