

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .features_dict import FeaturesDict


class ItisVipRestData(UniversalBaseModel):
    id: int
    description: str
    thumbnail: str
    features: FeaturesDict
    doi: typing.Optional[str] = None
    license_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="licenseVersion"), pydantic.Field(alias="licenseVersion")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
