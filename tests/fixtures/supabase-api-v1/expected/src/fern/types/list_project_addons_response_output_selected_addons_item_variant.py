

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .list_project_addons_response_output_selected_addons_item_variant_id import (
    ListProjectAddonsResponseOutputSelectedAddonsItemVariantId,
)
from .list_project_addons_response_output_selected_addons_item_variant_price import (
    ListProjectAddonsResponseOutputSelectedAddonsItemVariantPrice,
)


class ListProjectAddonsResponseOutputSelectedAddonsItemVariant(UniversalBaseModel):
    id: ListProjectAddonsResponseOutputSelectedAddonsItemVariantId
    name: str
    price: ListProjectAddonsResponseOutputSelectedAddonsItemVariantPrice
    meta: typing.Optional["JsonValueOutput"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value_output import JsonValueOutput

update_forward_refs(ListProjectAddonsResponseOutputSelectedAddonsItemVariant, JsonValueOutput=JsonValueOutput)
