

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_reference_param_type import ItemReferenceParamType


class ItemReferenceParam(UniversalBaseModel):
    """
    An internal identifier for an item to reference.
    """

    type: typing.Optional[ItemReferenceParamType] = pydantic.Field(default=None)
    """
    The type of item to reference. Always `item_reference`.
    """

    id: str = pydantic.Field()
    """
    The ID of the item to reference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
