

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_search_form_instance_provider_type import EntitySearchFormInstanceProviderType


class EntitySearchFormInstanceProvider(UniversalBaseModel):
    target_field_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="targetFieldKey"),
        pydantic.Field(
            alias="targetFieldKey",
            description="Where the entities that we search for should be populated within our form. Note here that we inherit any considerations and limitations on the values these entities can take on, like schemaId, from the definition of the field we're routing them to.",
        ),
    ] = None
    """
    Where the entities that we search for should be populated within our form. Note here that we inherit any considerations and limitations on the values these entities can take on, like schemaId, from the definition of the field we're routing them to.
    """

    type: typing.Optional[EntitySearchFormInstanceProviderType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
