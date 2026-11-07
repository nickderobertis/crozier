

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .not_found_error_body_extra import NotFoundErrorBodyExtra


class NotFoundErrorBody(UniversalBaseModel):
    """
    Not Found Exception
    """

    status_code: int
    detail: str
    extra: typing.Optional[NotFoundErrorBodyExtra] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
