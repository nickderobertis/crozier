

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AddComposableToCartRequestDataAttributesComponentsItem(UniversalBaseModel):
    meta: typing.Optional[typing.Any] = None
    purchasable_id: typing.Optional[float] = None
    purchasable_type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
