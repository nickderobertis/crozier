

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .kitty_gender import KittyGender
from .kitty_status import KittyStatus
from .parent import Parent


class Kitty(UniversalBaseModel):
    owner: typing.Optional[str] = pydantic.Field(default=None)
    """
    address of owner
    """

    dna: typing.Optional[str] = pydantic.Field(default=None)
    """
    should be string, as js can't handle long format
    """

    name: typing.Optional[str] = None
    gender: typing.Optional[KittyGender] = None
    mom: typing.Optional[Parent] = None
    dad: typing.Optional[Parent] = None
    breedings: typing.Optional[float] = None
    status: typing.Optional[KittyStatus] = None
    for_sale: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="forSale"), pydantic.Field(alias="forSale")
    ] = None
    price: typing.Optional[float] = pydantic.Field(default=None)
    """
    if not present, will be considered not for sale
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
