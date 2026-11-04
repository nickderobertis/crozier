

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bbox_crs import BboxCrs


class BboxCrsFilter(UniversalBaseModel):
    bbox_crs: typing_extensions.Annotated[
        typing.Optional[BboxCrs], FieldMetadata(alias="bboxCrs"), pydantic.Field(alias="bboxCrs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
