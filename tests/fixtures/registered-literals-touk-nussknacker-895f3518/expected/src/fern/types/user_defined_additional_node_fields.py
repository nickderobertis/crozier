

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .layout_data import LayoutData


class UserDefinedAdditionalNodeFields(UniversalBaseModel):
    description: typing.Optional[str] = None
    layout_data: typing_extensions.Annotated[
        typing.Optional[LayoutData], FieldMetadata(alias="layoutData"), pydantic.Field(alias="layoutData")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
