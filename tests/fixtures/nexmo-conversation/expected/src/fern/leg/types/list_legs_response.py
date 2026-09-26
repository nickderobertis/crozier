

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.page_size import PageSize
from ...types.record_index import RecordIndex
from .list_legs_response_embedded import ListLegsResponseEmbedded
from .list_legs_response_links import ListLegsResponseLinks


class ListLegsResponse(UniversalBaseModel):
    """
    List Legs Response Payload Object
    """

    embedded: typing_extensions.Annotated[
        ListLegsResponseEmbedded,
        FieldMetadata(alias="_embedded"),
        pydantic.Field(
            alias="_embedded",
            description="A list of conversation objects. See the [get details of a specific conversation](#retrieveConversation) response fields for a description of the nested objects",
        ),
    ]
    """
    A list of conversation objects. See the [get details of a specific conversation](#retrieveConversation) response fields for a description of the nested objects
    """

    links: typing_extensions.Annotated[
        ListLegsResponseLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")
    ]
    count: float = pydantic.Field()
    """
    The total number of records returned by your request.
    """

    page_size: PageSize
    record_index: RecordIndex

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
