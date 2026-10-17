

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_project_addons_response_output_available_addons_item import (
    ListProjectAddonsResponseOutputAvailableAddonsItem,
)
from .list_project_addons_response_output_selected_addons_item import ListProjectAddonsResponseOutputSelectedAddonsItem


class ListProjectAddonsResponseOutput(UniversalBaseModel):
    selected_addons: typing.List[ListProjectAddonsResponseOutputSelectedAddonsItem]
    available_addons: typing.List[ListProjectAddonsResponseOutputAvailableAddonsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
