

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LocationLocation(UniversalBaseModel):
    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address of the location. Only displayed if `name` is present.
    """

    lat: float = pydantic.Field()
    """
    Latitude of the location.
    """

    long_: typing_extensions.Annotated[
        float, FieldMetadata(alias="long"), pydantic.Field(alias="long", description="Longitude of the location.")
    ]
    """
    Longitude of the location.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
