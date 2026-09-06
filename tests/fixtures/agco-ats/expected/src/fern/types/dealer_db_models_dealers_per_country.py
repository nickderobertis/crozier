

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DealerDbModelsDealersPerCountry(UniversalBaseModel):
    count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="Count"), pydantic.Field(alias="Count")
    ] = None
    country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Country"), pydantic.Field(alias="Country")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
