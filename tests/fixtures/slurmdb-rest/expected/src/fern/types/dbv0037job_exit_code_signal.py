

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobExitCodeSignal(UniversalBaseModel):
    """
    Signal details (if signaled)
    """

    signal_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Signal number process received
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of signal received
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
