

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Aliases(UniversalBaseModel):
    """
    A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity",
            description="The number of CNAME aliases, if any, that you want to associate with this distribution.",
        ),
    ]
    """
    The number of CNAME aliases, if any, that you want to associate with this distribution.
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.",
        ),
    ] = None
    """
    A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
