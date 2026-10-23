

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_datasets_dataset_name_search_response_items_item import PostDatasetsDatasetNameSearchResponseItemsItem


class PostDatasetsDatasetNameSearchResponse(UniversalBaseModel):
    amount: typing.Optional[int] = None
    items: typing.Optional[typing.List[PostDatasetsDatasetNameSearchResponseItemsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
