

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identity_property_type import IdentityPropertyType
from .identity_property_value import IdentityPropertyValue


class IdentityProperty(UniversalBaseModel):
    """
    A property of an identity
    """

    key: str = pydantic.Field()
    """
    The key of the property
    """

    value: IdentityPropertyValue = pydantic.Field()
    """
    The value of the property
    """

    type: IdentityPropertyType = pydantic.Field()
    """
    The type of the property
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
