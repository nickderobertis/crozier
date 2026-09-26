

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_response_errors_item import BadRequestResponseErrorsItem


class BadRequestResponse(UniversalBaseModel):
    """
    The request body did not match the expected payload.
    """

    errors: typing.Optional[typing.List[BadRequestResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
