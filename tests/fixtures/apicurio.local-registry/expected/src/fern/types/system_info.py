

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SystemInfo(UniversalBaseModel):
    """ """

    built_on: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="builtOn")] = None
    description: typing.Optional[str] = None
    name: typing.Optional[str] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
