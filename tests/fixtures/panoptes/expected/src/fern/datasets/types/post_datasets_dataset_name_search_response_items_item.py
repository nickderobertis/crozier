

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostDatasetsDatasetNameSearchResponseItemsItem(UniversalBaseModel):
    item_id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    tags: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
