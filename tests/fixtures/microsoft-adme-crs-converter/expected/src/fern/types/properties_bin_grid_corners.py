

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .point_properties import PointProperties


class PropertiesBinGridCorners(UniversalBaseModel):
    kind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Kind"), pydantic.Field(alias="Kind")
    ] = None
    point_properties: typing_extensions.Annotated[
        typing.Optional[typing.List[PointProperties]],
        FieldMetadata(alias="PointProperties"),
        pydantic.Field(alias="PointProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
