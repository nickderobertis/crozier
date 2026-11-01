

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sku_name import SkuName


class Sku(UniversalBaseModel):
    """
    The Sku.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="The display name of the sku."),
    ] = None
    """
    The display name of the sku.
    """

    family: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sku family.
    """

    name: SkuName = pydantic.Field()
    """
    The sku name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
