

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDestinyEquipItemResult(UniversalBaseModel):
    """
    The results of an Equipping operation performed through the Destiny API.
    """

    equip_status: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="equipStatus"),
        pydantic.Field(
            alias="equipStatus",
            description="A PlatformErrorCodes enum indicating whether it succeeded, and if it failed why.",
        ),
    ] = None
    """
    A PlatformErrorCodes enum indicating whether it succeeded, and if it failed why.
    """

    item_instance_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemInstanceId"),
        pydantic.Field(
            alias="itemInstanceId",
            description="The instance ID of the item in question (all items that can be equipped must, but definition, be Instanced and thus have an Instance ID that you can use to refer to them)",
        ),
    ] = None
    """
    The instance ID of the item in question (all items that can be equipped must, but definition, be Instanced and thus have an Instance ID that you can use to refer to them)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
