

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_tags_for_resource_result_tags_items_item import ListTagsForResourceResultTagsItemsItem


class ListTagsForResourceResultTags(UniversalBaseModel):
    """
    A complex type that contains zero or more <code>Tag</code> elements.
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[ListTagsForResourceResultTagsItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(alias="Items", description=" A complex type that contains <code>Tag</code> elements."),
    ] = None
    """
     A complex type that contains <code>Tag</code> elements.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
