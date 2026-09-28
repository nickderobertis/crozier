

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RequiresReconsentInfoPoliciesItem(UniversalBaseModel):
    slug: str
    old_version: typing_extensions.Annotated[str, FieldMetadata(alias="oldVersion"), pydantic.Field(alias="oldVersion")]
    new_version: typing_extensions.Annotated[str, FieldMetadata(alias="newVersion"), pydantic.Field(alias="newVersion")]
    sha256: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
