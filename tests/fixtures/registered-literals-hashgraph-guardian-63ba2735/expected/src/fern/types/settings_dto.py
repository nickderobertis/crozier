

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SettingsDto(UniversalBaseModel):
    ipfs_storage_api_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="ipfsStorageApiKey"), pydantic.Field(alias="ipfsStorageApiKey")
    ]
    operator_id: typing_extensions.Annotated[str, FieldMetadata(alias="operatorId"), pydantic.Field(alias="operatorId")]
    operator_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="operatorKey"), pydantic.Field(alias="operatorKey")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
