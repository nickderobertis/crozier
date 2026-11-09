

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_relationship_type import CaseRelationshipType
from .source_structured_data import SourceStructuredData


class RelatedCase(UniversalBaseModel):
    additional_source_data: typing_extensions.Annotated[
        typing.Optional[SourceStructuredData],
        FieldMetadata(alias="additionalSourceData"),
        pydantic.Field(alias="additionalSourceData"),
    ] = None
    case_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseAPI"),
        pydantic.Field(alias="caseAPI", description="Link to the Case API of the current related case."),
    ] = None
    """
    Link to the Case API of the current related case.
    """

    case_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseId"),
        pydantic.Field(
            alias="caseId",
            description="Case ID of the related Case. This can be null if this case in not found in our database. However the meta information of the related case will be present.",
        ),
    ] = None
    """
    Case ID of the related Case. This can be null if this case in not found in our database. However the meta information of the related case will be present.
    """

    case_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseName"),
        pydantic.Field(alias="caseName", description="Case Name of the related Case."),
    ] = None
    """
    Case Name of the related Case.
    """

    case_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseNumber"),
        pydantic.Field(alias="caseNumber", description="Case Number of the related Case."),
    ]
    """
    Case Number of the related Case.
    """

    case_relationship_type: typing_extensions.Annotated[
        typing.Optional[CaseRelationshipType],
        FieldMetadata(alias="caseRelationshipType"),
        pydantic.Field(alias="caseRelationshipType"),
    ] = None
    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible",
            description="This specifies if the related cases is still related to the parent case or not.",
        ),
    ]
    """
    This specifies if the related cases is still related to the parent case or not.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    source_case_relationship_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourceCaseRelationshipType"),
        pydantic.Field(alias="sourceCaseRelationshipType", description="Case Relationship Type provided by court."),
    ]
    """
    Case Relationship Type provided by court.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
