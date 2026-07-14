

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImportError(UniversalBaseModel):
    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The filename
    """

    import_error_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The import error ID.
    """

    stack_trace: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full stackstrace..
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when this error was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
