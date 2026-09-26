

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SessionPromptRequestModel(UniversalBaseModel):
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerID"), pydantic.Field(alias="providerID")]
    model_id: typing_extensions.Annotated[str, FieldMetadata(alias="modelID"), pydantic.Field(alias="modelID")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
