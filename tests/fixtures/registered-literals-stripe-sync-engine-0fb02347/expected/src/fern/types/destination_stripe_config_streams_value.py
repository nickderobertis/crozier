

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinationStripeConfigStreamsValue(UniversalBaseModel):
    plural_name: str = pydantic.Field()
    """
    Stripe Custom Object api_name_plural
    """

    field_mapping: typing.Dict[str, str] = pydantic.Field()
    """
    Mapping from Custom Object field names to source record fields.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
