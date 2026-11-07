

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .index_mode import IndexMode


class StateResponse(UniversalBaseModel):
    version: str = pydantic.Field()
    """
    Walletd semantic version.
    """

    commit: str = pydantic.Field()
    """
    Git commit hash walletd was built from.
    """

    os: str = pydantic.Field()
    """
    Operating system of the running binary.
    """

    build_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="buildTime"),
        pydantic.Field(alias="buildTime", description="Build timestamp embedded in the binary."),
    ]
    """
    Build timestamp embedded in the binary.
    """

    start_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="Time when walletd started."),
    ]
    """
    Time when walletd started.
    """

    index_mode: typing_extensions.Annotated[
        IndexMode, FieldMetadata(alias="indexMode"), pydantic.Field(alias="indexMode")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
