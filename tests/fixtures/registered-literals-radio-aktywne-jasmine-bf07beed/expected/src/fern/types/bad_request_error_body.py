

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_error_body_extra import BadRequestErrorBodyExtra


class BadRequestErrorBody(UniversalBaseModel):
    """
    Validation Exception
    """

    status_code: int
    detail: str
    extra: typing.Optional[BadRequestErrorBodyExtra] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
