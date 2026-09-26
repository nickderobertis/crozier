

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalIntegrationCredentialsResolveTargetSecretsResponseTargetsItem(UniversalBaseModel):
    target_key: typing_extensions.Annotated[str, FieldMetadata(alias="targetKey"), pydantic.Field(alias="targetKey")]
    secrets: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
