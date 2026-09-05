

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProductUiGet(UniversalBaseModel):
    product_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="productName"), pydantic.Field(alias="productName")
    ]
    ui: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Front-end owned ui product configuration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
