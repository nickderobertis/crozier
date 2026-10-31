

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunMaintenanceRequestGc(UniversalBaseModel):
    """
    A garbage collection job for aged, unreferenced objects, which also collects the grep
    index's objects when the deployment maintains a grep index.
    """

    grace_window_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The minimum age, in milliseconds, that an object must reach before the pass can delete it.
    The value must be at least the server's advertised safety floor. The grep index's collector
    keeps its own age rules, so this value doesn't change them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
