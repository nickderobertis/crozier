

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SuperFundProduct(UniversalBaseModel):
    abn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ABN"),
        pydantic.Field(alias="ABN", description="The ABN of the Regulated SuperFund"),
    ] = None
    """
    The ABN of the Regulated SuperFund
    """

    product_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ProductName"),
        pydantic.Field(alias="ProductName", description="The name of the Regulated SuperFund"),
    ] = None
    """
    The name of the Regulated SuperFund
    """

    spin: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SPIN"),
        pydantic.Field(
            alias="SPIN",
            description="The SPIN of the Regulated SuperFund. This field has been deprecated. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN",
        ),
    ] = None
    """
    The SPIN of the Regulated SuperFund. This field has been deprecated. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN
    """

    usi: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="USI"),
        pydantic.Field(alias="USI", description="The USI of the Regulated SuperFund"),
    ] = None
    """
    The USI of the Regulated SuperFund
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
