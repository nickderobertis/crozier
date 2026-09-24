

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .created_at_field import CreatedAtField
from .fleet_links import FleetLinks
from .updated_at_field import UpdatedAtField


class Fleet(UpdatedAtField, CreatedAtField):
    links: typing_extensions.Annotated[FleetLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Fleet
    """

    id: str = pydantic.Field()
    """
    The id of the Fleet
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the Fleet
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
