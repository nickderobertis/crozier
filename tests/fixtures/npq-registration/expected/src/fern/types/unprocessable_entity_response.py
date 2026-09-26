

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .unprocessable_entity_response_errors_item import UnprocessableEntityResponseErrorsItem


class UnprocessableEntityResponse(UniversalBaseModel):
    """
    The payload was not valid. See the errors for more information.
    """

    errors: typing.Optional[typing.List[UnprocessableEntityResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
