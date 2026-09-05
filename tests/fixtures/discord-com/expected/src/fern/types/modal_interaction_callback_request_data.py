

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_row_component_for_modal_request import ActionRowComponentForModalRequest


class ModalInteractionCallbackRequestData(UniversalBaseModel):
    custom_id: str
    title: str
    components: typing.List[ActionRowComponentForModalRequest]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
