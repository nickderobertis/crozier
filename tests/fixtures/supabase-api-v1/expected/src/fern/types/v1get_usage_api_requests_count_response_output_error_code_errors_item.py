

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V1GetUsageApiRequestsCountResponseOutputErrorCodeErrorsItem(UniversalBaseModel):
    domain: str
    location: str
    location_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="locationType"), pydantic.Field(alias="locationType")
    ]
    message: str
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
