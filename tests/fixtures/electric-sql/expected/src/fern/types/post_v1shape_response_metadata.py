

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostV1ShapeResponseMetadata(UniversalBaseModel):
    """
    PostgreSQL snapshot metadata.
    """

    xmin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Minimum transaction ID in the snapshot.
    """

    xmax: typing.Optional[str] = pydantic.Field(default=None)
    """
    Maximum transaction ID in the snapshot.
    """

    xip_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Transaction IDs in progress during snapshot.
    """

    snapshot_mark: typing.Optional[int] = pydantic.Field(default=None)
    """
    Random number identifying this snapshot.
    """

    database_lsn: typing.Optional[str] = pydantic.Field(default=None)
    """
    Database LSN at snapshot time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
