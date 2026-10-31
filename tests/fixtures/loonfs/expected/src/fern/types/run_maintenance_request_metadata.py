

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunMaintenanceRequestMetadata(UniversalBaseModel):
    """
    A job that folds the WAL tail and compacts metadata until nothing is due, or until the job
    reaches its work limit.
    """

    max_wal_tail_objects: typing.Optional[int] = pydantic.Field(default=None)
    """
    The WAL tail length, in WAL objects, that triggers a fold. Omit it to use the server
    default.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
