

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PageCreatePageResponseStatusMonitorListItem(UniversalBaseModel):
    id: str
    show_current: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showCurrent"), pydantic.Field(alias="showCurrent")
    ] = None
    show_detail: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showDetail"), pydantic.Field(alias="showDetail")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
