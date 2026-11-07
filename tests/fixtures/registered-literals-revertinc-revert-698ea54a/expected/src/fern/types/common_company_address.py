

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonCompanyAddress(UniversalBaseModel):
    street: typing.Optional[str] = None
    city: str
    state: str
    country: str
    zip: str
    postal_code: typing_extensions.Annotated[str, FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
