

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .list_project_addons_response_output_available_addons_item_variants_item_id import (
    ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemId,
)
from .list_project_addons_response_output_available_addons_item_variants_item_price import (
    ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPrice,
)


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItem(UniversalBaseModel):
    id: ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemId
    name: str
    price: ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPrice
    meta: typing.Optional["JsonValueOutput"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value_output import JsonValueOutput

update_forward_refs(ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItem, JsonValueOutput=JsonValueOutput)
