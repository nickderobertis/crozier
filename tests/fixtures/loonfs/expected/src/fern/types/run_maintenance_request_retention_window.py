

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunMaintenanceRequestRetentionWindow(UniversalBaseModel):
    """
    A job that sets or clears the namespace's retention window.
    """

    retention_window_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The namespace's new retention window, in milliseconds, which must be positive. Without it,
    the job clears the namespace's window, and the reference server's `retention_window_ms`
    setting applies to the namespace again.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
