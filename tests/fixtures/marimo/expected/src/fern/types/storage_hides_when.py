

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_hides_when_kind import StorageHidesWhenKind


class StorageHidesWhen(UniversalBaseModel):
    """
    Hide this suggestion when a live storage namespace matches.
    """

    backend_types: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="backendTypes"), pydantic.Field(alias="backendTypes")
    ]
    kind: StorageHidesWhenKind
    protocols: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
