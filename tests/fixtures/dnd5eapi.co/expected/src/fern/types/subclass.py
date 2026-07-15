

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .api_reference import ApiReference
from .resource_description import ResourceDescription
from .subclass_spells_item import SubclassSpellsItem


class Subclass(ApiReference, ResourceDescription):
    """
    `Subclass`
    """

    class_: typing_extensions.Annotated[typing.Optional[ApiReference], FieldMetadata(alias="class")] = None
    spells: typing.Optional[typing.List[SubclassSpellsItem]] = None
    subclass_flavor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lore-friendly flavor text for a classes respective subclass.
    """

    subclass_levels: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource url that shows the subclass level progression.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
