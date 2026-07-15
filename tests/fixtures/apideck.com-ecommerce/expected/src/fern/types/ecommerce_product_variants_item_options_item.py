

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EcommerceProductVariantsItemOptionsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the option of the variant.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the option for the variant.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the option for the variant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
