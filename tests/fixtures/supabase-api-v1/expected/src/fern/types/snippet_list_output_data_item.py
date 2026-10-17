

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snippet_list_output_data_item_owner import SnippetListOutputDataItemOwner
from .snippet_list_output_data_item_project import SnippetListOutputDataItemProject
from .snippet_list_output_data_item_type import SnippetListOutputDataItemType
from .snippet_list_output_data_item_updated_by import SnippetListOutputDataItemUpdatedBy
from .snippet_list_output_data_item_visibility import SnippetListOutputDataItemVisibility


class SnippetListOutputDataItem(UniversalBaseModel):
    id: str
    inserted_at: str
    updated_at: str
    type: SnippetListOutputDataItemType
    visibility: SnippetListOutputDataItemVisibility
    name: str
    description: typing.Optional[str] = None
    project: SnippetListOutputDataItemProject
    owner: SnippetListOutputDataItemOwner
    updated_by: SnippetListOutputDataItemUpdatedBy
    favorite: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
