

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SignalWarning(UniversalBaseModel):
    """
    Conveys information about the errors causing missing or stale bank data used to construct the /signal/evaluate scores and response
    """

    warning_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The particular warning code.
    """

    warning_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A developer-friendly representation of the warning code.
    """

    warning_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Broad categorization of the warning.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
