

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mapping_settings import MappingSettings
from .transform_settings_location import TransformSettingsLocation


class TransformSettings(UniversalBaseModel):
    """
    Settings to transform a JWT token and its location
    """

    location: TransformSettingsLocation
    mapping_settings: typing_extensions.Annotated[MappingSettings, FieldMetadata(alias="mappingSettings")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
