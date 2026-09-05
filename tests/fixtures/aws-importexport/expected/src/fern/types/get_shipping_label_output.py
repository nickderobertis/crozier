

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .generic_string import GenericString


class GetShippingLabelOutput(UniversalBaseModel):
    shipping_label_url: typing_extensions.Annotated[
        typing.Optional[GenericString],
        FieldMetadata(alias="ShippingLabelURL"),
        pydantic.Field(alias="ShippingLabelURL"),
    ] = None
    warning: typing_extensions.Annotated[
        typing.Optional[GenericString], FieldMetadata(alias="Warning"), pydantic.Field(alias="Warning")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
