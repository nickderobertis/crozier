

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MappingSettings(UniversalBaseModel):
    """
    Settings to change fields of a JWT token
    """

    map_: typing_extensions.Annotated[typing.Dict[str, str], FieldMetadata(alias="map")] = pydantic.Field()
    """
    Fields to rename
    """

    remove: typing.List[str] = pydantic.Field()
    """
    Fields to remove
    """

    values: typing.Dict[str, str] = pydantic.Field()
    """
    Fields to set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
