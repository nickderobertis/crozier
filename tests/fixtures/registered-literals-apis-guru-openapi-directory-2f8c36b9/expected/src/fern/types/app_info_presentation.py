

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AppInfoPresentation(UniversalBaseModel):
    branch: typing.Optional[str] = None
    commit_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="commitTime"), pydantic.Field(alias="commitTime")
    ] = None
    name: typing.Optional[str] = None
    production_mode: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="productionMode"), pydantic.Field(alias="productionMode")
    ] = None
    revision: typing.Optional[str] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
