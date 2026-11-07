

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MonitorClean(UniversalBaseModel):
    """
    report on cleaning dups out of monitors
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address being cleaned
    """

    size_then: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sizeThen"),
        pydantic.Field(alias="sizeThen", description="the number of appearances in the monitor prior to cleaning"),
    ] = None
    """
    the number of appearances in the monitor prior to cleaning
    """

    size_now: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sizeNow"),
        pydantic.Field(alias="sizeNow", description="the number of appearances in the monitor after cleaning"),
    ] = None
    """
    the number of appearances in the monitor after cleaning
    """

    dups: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of duplicates removed
    """

    staged: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if the address is in the stage, `false` otherwise
    """

    removed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if the address was removed from the stage, `false` otherwise
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
