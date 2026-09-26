

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2error_error_details import V2ErrorErrorDetails


class V2ErrorError(UniversalBaseModel):
    """
    Canonical error details.
    """

    code: str = pydantic.Field()
    """
    Stable machine-readable error code.
    """

    message: str = pydantic.Field()
    """
    Human-readable explanation of the error.
    """

    details: typing.Optional[V2ErrorErrorDetails] = pydantic.Field(default=None)
    """
    Structured error context whose keys depend on the error. Actionable `403` responses use the `V2ActionableForbiddenDetails` shape; validation failures may return issue arrays instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
