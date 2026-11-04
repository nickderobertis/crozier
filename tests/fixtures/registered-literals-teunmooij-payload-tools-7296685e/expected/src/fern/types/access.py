

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_collections_value import AccessCollectionsValue


class Access(UniversalBaseModel):
    can_access_admin: typing_extensions.Annotated[
        bool, FieldMetadata(alias="canAccessAdmin"), pydantic.Field(alias="canAccessAdmin")
    ]
    collections: typing.Dict[str, AccessCollectionsValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
