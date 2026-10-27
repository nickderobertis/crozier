

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VersionContainer(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the versioned component
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version id of the component
    """

    build_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="buildTime"), pydantic.Field(alias="buildTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
