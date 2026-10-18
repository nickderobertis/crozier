

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_project_addons_response_output_available_addons_item_type import (
    ListProjectAddonsResponseOutputAvailableAddonsItemType,
)
from .list_project_addons_response_output_available_addons_item_variants_item import (
    ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItem,
)


class ListProjectAddonsResponseOutputAvailableAddonsItem(UniversalBaseModel):
    type: ListProjectAddonsResponseOutputAvailableAddonsItemType
    name: str
    variants: typing.List[ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
