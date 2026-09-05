

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .view_options_options_options import ViewOptionsOptionsOptions
from .view_options_options_view_type import ViewOptionsOptionsViewType


class ViewOptionsOptions(UniversalBaseModel):
    view_type: typing_extensions.Annotated[
        ViewOptionsOptionsViewType, FieldMetadata(alias="viewType"), pydantic.Field(alias="viewType")
    ]
    options: ViewOptionsOptionsOptions
    freeze_columns: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="freezeColumns"), pydantic.Field(alias="freezeColumns")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
