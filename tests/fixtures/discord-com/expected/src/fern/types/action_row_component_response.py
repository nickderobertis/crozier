

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_row_component_response_components_item import ActionRowComponentResponseComponentsItem


class ActionRowComponentResponse(UniversalBaseModel):
    type: int
    id: int
    components: typing.Optional[typing.List[ActionRowComponentResponseComponentsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
