

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .kiln import Kiln
from .load_noted_kiln import LoadNotedKiln
from .load_reserved_kiln import LoadReservedKiln


class Load(UniversalBaseModel):
    label: str
    kiln: Kiln
    overflow_kiln: typing_extensions.Annotated[
        typing.Optional[Kiln], FieldMetadata(alias="overflowKiln"), pydantic.Field(alias="overflowKiln")
    ] = None
    usual_kiln: typing_extensions.Annotated[
        typing.Optional[Kiln], FieldMetadata(alias="usualKiln"), pydantic.Field(alias="usualKiln")
    ] = None
    solo_kiln: typing_extensions.Annotated[
        typing.Optional[Kiln], FieldMetadata(alias="soloKiln"), pydantic.Field(alias="soloKiln")
    ] = None
    noted_kiln: typing_extensions.Annotated[
        typing.Optional[LoadNotedKiln],
        FieldMetadata(alias="notedKiln"),
        pydantic.Field(alias="notedKiln", description="Kiln named in the firing log."),
    ] = None
    """
    Kiln named in the firing log.
    """

    reserved_kiln: typing_extensions.Annotated[
        typing.Optional[LoadReservedKiln], FieldMetadata(alias="reservedKiln"), pydantic.Field(alias="reservedKiln")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
