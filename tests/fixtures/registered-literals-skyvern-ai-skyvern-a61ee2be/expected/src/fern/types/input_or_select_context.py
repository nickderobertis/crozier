

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InputOrSelectContext(UniversalBaseModel):
    intention: typing.Optional[str] = None
    field: typing.Optional[str] = None
    is_required: typing.Optional[bool] = None
    is_search_bar: typing.Optional[bool] = None
    is_location_input: typing.Optional[bool] = None
    is_date_related: typing.Optional[bool] = None
    date_format: typing.Optional[str] = None
    is_text_captcha: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
