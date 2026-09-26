

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateStruct(UniversalBaseModel):
    contact_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactEmail"),
        pydantic.Field(
            alias="contactEmail", description="Updated email address of the merchant's primary contact. Optional."
        ),
    ] = None
    """
    Updated email address of the merchant's primary contact. Optional.
    """

    contact_first: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactFirst"),
        pydantic.Field(
            alias="contactFirst", description="Updated first name of the merchant's primary contact. Optional."
        ),
    ] = None
    """
    Updated first name of the merchant's primary contact. Optional.
    """

    contact_last: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactLast"),
        pydantic.Field(
            alias="contactLast", description="Updated last name of the merchant's primary contact. Optional."
        ),
    ] = None
    """
    Updated last name of the merchant's primary contact. Optional.
    """

    merchant_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="merchantName"),
        pydantic.Field(
            alias="merchantName",
            description="New legal or trading name of the merchant business. Required; must be 1–255 characters.",
        ),
    ]
    """
    New legal or trading name of the merchant business. Required; must be 1–255 characters.
    """

    reference_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="referenceId"),
        pydantic.Field(alias="referenceId", description="The ID you use in your own system to identify this merchant."),
    ] = None
    """
    The ID you use in your own system to identify this merchant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
