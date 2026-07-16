

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mapping_settings import MappingSettings


class VerificationSettings(UniversalBaseModel):
    """
    Settings to verify the value of JWT token fields
    """

    fields: typing.Dict[str, str] = pydantic.Field()
    """
    Fields to verify with their values
    """

    mapping_settings: typing_extensions.Annotated[
        typing.Optional[MappingSettings],
        FieldMetadata(alias="mappingSettings"),
        pydantic.Field(alias="mappingSettings"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
