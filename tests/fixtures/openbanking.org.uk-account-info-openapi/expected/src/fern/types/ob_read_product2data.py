

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item import ObReadProduct2DataProductItem


class ObReadProduct2Data(UniversalBaseModel):
    """
    Aligning with the read write specs structure.
    """

    product: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadProduct2DataProductItem]], FieldMetadata(alias="Product")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
