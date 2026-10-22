

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContactAttribute(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the contact attribute
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the contact attribute was created"),
    ]
    """
    The date and time the contact attribute was created
    """

    updated_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the contact attribute was last updated"),
    ]
    """
    The date and time the contact attribute was last updated
    """

    attribute_key_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="attributeKeyId"),
        pydantic.Field(alias="attributeKeyId", description="The ID of the attribute key"),
    ]
    """
    The ID of the attribute key
    """

    contact_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="contactId"), pydantic.Field(alias="contactId", description="The ID of the contact")
    ]
    """
    The ID of the contact
    """

    value: str = pydantic.Field()
    """
    The value of the attribute
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
