

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Monitor(UniversalBaseModel):
    """
    a local file indicating a user's interest in an address. Includes caches for reconicilations, transactions, and appearances as well as an optional association to named account
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of this monitor
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the name of this monitor (if any)
    """

    n_records: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nRecords"),
        pydantic.Field(alias="nRecords", description="the number of appearances for this monitor"),
    ] = None
    """
    the number of appearances for this monitor
    """

    file_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="fileSize"),
        pydantic.Field(alias="fileSize", description="the size of this monitor on disc"),
    ] = None
    """
    the size of this monitor on disc
    """

    last_scanned: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastScanned"),
        pydantic.Field(alias="lastScanned", description="the last scanned block number"),
    ] = None
    """
    the last scanned block number
    """

    is_empty: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isEmpty"),
        pydantic.Field(alias="isEmpty", description="`true` if the monitor has no appearances, `false` otherwise"),
    ] = None
    """
    `true` if the monitor has no appearances, `false` otherwise
    """

    is_staged: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isStaged"),
        pydantic.Field(alias="isStaged", description="`true` if the monitor file in on the stage, `false` otherwise"),
    ] = None
    """
    `true` if the monitor file in on the stage, `false` otherwise
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if this monitor has been deleted, `false` otherwise
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
