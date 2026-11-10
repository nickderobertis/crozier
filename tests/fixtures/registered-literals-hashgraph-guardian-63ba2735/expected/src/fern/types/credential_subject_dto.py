

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CredentialSubjectDto(UniversalBaseModel):
    geography: str
    law: str
    tags: str
    isic: typing_extensions.Annotated[str, FieldMetadata(alias="ISIC"), pydantic.Field(alias="ISIC")]
    context: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="@context"), pydantic.Field(alias="@context")
    ]
    id: str
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
