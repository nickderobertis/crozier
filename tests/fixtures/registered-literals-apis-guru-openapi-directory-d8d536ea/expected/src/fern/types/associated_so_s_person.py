

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .associated_so_s_person_entity_type import AssociatedSoSPersonEntityType
from .contact import Contact


class AssociatedSoSPerson(UniversalBaseModel):
    contact: Contact
    entity_name: typing_extensions.Annotated[str, FieldMetadata(alias="entityName"), pydantic.Field(alias="entityName")]
    entity_type: typing_extensions.Annotated[
        AssociatedSoSPersonEntityType, FieldMetadata(alias="entityType"), pydantic.Field(alias="entityType")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
