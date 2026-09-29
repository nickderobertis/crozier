

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_value import JsonValue
from .ui_message_response_parts_item import UiMessageResponsePartsItem
from .ui_message_response_role import UiMessageResponseRole


class UiMessageResponse(UniversalBaseModel):
    id: str
    role: UiMessageResponseRole
    parts: typing.List[UiMessageResponsePartsItem]
    metadata: typing.Optional[typing.Dict[str, typing.Optional[JsonValue]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
