

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_error_body_errors_parameters import BadRequestErrorBodyErrorsParameters


class BadRequestErrorBodyErrors(UniversalBaseModel):
    """
    Map that sums up all received values that seemed incorrect
    """

    fields: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    All input fields that seemed incorrect
    """

    parameters: typing.Optional[BadRequestErrorBodyErrorsParameters] = pydantic.Field(default=None)
    """
    All query-, header- and path- parameters that seemed incorrect
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
