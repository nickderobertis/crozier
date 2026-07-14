

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApiErrorResponse(UniversalBaseModel):
    """
    Generic HTTP API error response
    """

    code: typing.Optional[int] = None
    detail: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Details structure for additional information about the error if available. Content and structure will be error specific.
    """

    error_type: typing.Optional[str] = None
    message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
