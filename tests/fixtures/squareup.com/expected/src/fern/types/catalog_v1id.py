

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CatalogV1Id(UniversalBaseModel):
    """
    A Square API V1 identifier of an item, including the object ID and its associated location ID.
    """

    catalog_v1id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="catalog_v1_id"),
        pydantic.Field(
            alias="catalog_v1_id",
            description="The ID for an object used in the Square API V1, if the object ID differs from the Square API V2 object ID.",
        ),
    ] = None
    """
    The ID for an object used in the Square API V1, if the object ID differs from the Square API V2 object ID.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the `Location` this Connect V1 ID is associated with.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
