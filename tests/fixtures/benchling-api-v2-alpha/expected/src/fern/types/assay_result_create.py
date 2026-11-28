

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assay_result_create_fields import AssayResultCreateFields
from .user_validation import UserValidation


class AssayResultCreate(UniversalBaseModel):
    field_validation: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, UserValidation]],
        FieldMetadata(alias="fieldValidation"),
        pydantic.Field(
            alias="fieldValidation", description="Dictionary mapping field names to UserValidation Resources."
        ),
    ] = None
    """
    Dictionary mapping field names to UserValidation Resources.
    """

    fields: AssayResultCreateFields = pydantic.Field()
    """
    Dictionary of result fields. Please note the field keys must be the field's system name, not display name.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID
    """

    project_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="projectId"),
        pydantic.Field(
            alias="projectId",
            description="The project that the assay result should be uploaded to. Only users with read access to the project will be able to read the assay result. Leaving this empty will result in only the creator having read access.",
        ),
    ] = None
    """
    The project that the assay result should be uploaded to. Only users with read access to the project will be able to read the assay result. Leaving this empty will result in only the creator having read access.
    """

    schema_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="schemaId"),
        pydantic.Field(alias="schemaId", description="ID of result schema under which to upload this result"),
    ]
    """
    ID of result schema under which to upload this result
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
