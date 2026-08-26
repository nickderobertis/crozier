

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KernelCapabilitiesNotification(UniversalBaseModel):
    """
    Kernel capabilities detected at startup.

        All fields auto-detected in __post_init__.

        Attributes:
            terminal: Terminal access (unavailable on Windows/Pyodide).
            pylsp: Python Language Server Protocol installed.
            ty: ty type checker installed.
            basedpyright: basedpyright type checker installed.
    """

    basedpyright: typing.Optional[bool] = None
    pylsp: typing.Optional[bool] = None
    pyrefly: typing.Optional[bool] = None
    terminal: typing.Optional[bool] = None
    ty: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
