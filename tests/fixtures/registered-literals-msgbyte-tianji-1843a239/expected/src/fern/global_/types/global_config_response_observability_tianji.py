

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GlobalConfigResponseObservabilityTianji(UniversalBaseModel):
    base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="baseUrl"), pydantic.Field(alias="baseUrl")
    ] = None
    website_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="websiteId"), pydantic.Field(alias="websiteId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
