

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .meta import Meta
from .not_found_error_body_errors_item import NotFoundErrorBodyErrorsItem


class NotFoundErrorBody(UniversalBaseModel):
    errors: typing.List[NotFoundErrorBodyErrorsItem]
    meta: typing.Optional[Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
