

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetV1ShapeResponseDataMetadata(UniversalBaseModel):
    """
    PostgreSQL snapshot metadata for tracking which changes to skip.
    This response format is returned when any `subset__*` parameters are present in the request.
    """

    xmin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Minimum transaction ID in the snapshot (uint64 as string).
    """

    xmax: typing.Optional[str] = pydantic.Field(default=None)
    """
    Maximum transaction ID in the snapshot (uint64 as string).
    """

    xip_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of transaction IDs that were in progress during the snapshot (uint64 as strings).
    """

    snapshot_mark: typing.Optional[int] = pydantic.Field(default=None)
    """
    Random number identifying this snapshot, matching the value in operation headers.
    """

    database_lsn: typing.Optional[str] = pydantic.Field(default=None)
    """
    Database log sequence number at the time the snapshot was taken.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
