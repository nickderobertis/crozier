

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TaxResidency(UniversalBaseModel):
    country: str = pydantic.Field()
    """
    Land (ISO 3166-1)
    """

    is_primary: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPrimary"), pydantic.Field(alias="isPrimary")
    ] = None
    tin_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tinNumber"), pydantic.Field(alias="tinNumber")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
