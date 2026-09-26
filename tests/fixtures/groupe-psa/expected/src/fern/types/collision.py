

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .collision_links import CollisionLinks
from .collision_obj import CollisionObj
from .created_at_field import CreatedAtField
from .vin import Vin


class Collision(CreatedAtField, CollisionObj):
    id: str
    vin: Vin
    tipped_over: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="tippedOver"),
        pydantic.Field(
            alias="tippedOver",
            description="Indicates if the car tipped over during the collision. Warning : This information is applicable only on vehicles equipped with dedicated sensor and is optionnal.",
        ),
    ] = None
    """
    Indicates if the car tipped over during the collision. Warning : This information is applicable only on vehicles equipped with dedicated sensor and is optionnal.
    """

    pedestrian: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the collision involve a pedestrian. *Warning : This information is applicable only on vehicles equipped with dedicated sensor and is optionnal*
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    links: typing_extensions.Annotated[CollisionLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
