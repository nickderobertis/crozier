

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .geo_restriction import GeoRestriction


class Restrictions(UniversalBaseModel):
    """
    A complex type that identifies ways in which you want to restrict distribution of your content.
    """

    geo_restriction: typing_extensions.Annotated[
        GeoRestriction, FieldMetadata(alias="GeoRestriction"), pydantic.Field(alias="GeoRestriction")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
