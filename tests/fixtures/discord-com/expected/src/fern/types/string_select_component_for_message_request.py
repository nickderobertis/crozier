

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .string_select_option_for_message_request import StringSelectOptionForMessageRequest


class StringSelectComponentForMessageRequest(UniversalBaseModel):
    type: int
    custom_id: str
    placeholder: typing.Optional[str] = None
    min_values: typing.Optional[int] = None
    max_values: typing.Optional[int] = None
    disabled: typing.Optional[bool] = None
    options: typing.List[StringSelectOptionForMessageRequest]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
