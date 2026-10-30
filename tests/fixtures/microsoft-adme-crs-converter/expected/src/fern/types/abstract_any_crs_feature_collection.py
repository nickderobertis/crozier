

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .abstract_feature import AbstractFeature


class AbstractAnyCrsFeatureCollection(UniversalBaseModel):
    coordinate_reference_system_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CoordinateReferenceSystemID"),
        pydantic.Field(alias="CoordinateReferenceSystemID"),
    ] = None
    features: typing.Optional[typing.List[AbstractFeature]] = None
    persistable_reference_crs: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="persistableReferenceCrs"),
        pydantic.Field(alias="persistableReferenceCrs"),
    ] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
