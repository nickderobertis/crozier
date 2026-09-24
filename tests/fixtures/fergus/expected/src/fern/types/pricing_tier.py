

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class PricingTier(UniversalBaseModel):
    id: float
    name: str
    is_default: typing_extensions.Annotated[bool, FieldMetadata(alias="isDefault"), pydantic.Field(alias="isDefault")]
    tier_type: typing_extensions.Annotated[str, FieldMetadata(alias="tierType"), pydantic.Field(alias="tierType")]
    markup_rate: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="markupRate"), pydantic.Field(alias="markupRate")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
