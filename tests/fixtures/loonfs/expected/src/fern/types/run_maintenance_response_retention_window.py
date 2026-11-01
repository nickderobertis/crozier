

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId


class RunMaintenanceResponseRetentionWindow(UniversalBaseModel):
    """
    The namespace's retention window after the job.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace whose retention window the job set or cleared.
    """

    retention_window_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The namespace's retention window, in milliseconds. It's absent when the namespace has no
    window of its own.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
