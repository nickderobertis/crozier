

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .not_found_error_body_data import NotFoundErrorBodyData
from .not_found_error_body_name import NotFoundErrorBodyName


class NotFoundErrorBody(UniversalBaseModel):
    name: NotFoundErrorBodyName
    data: NotFoundErrorBodyData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
