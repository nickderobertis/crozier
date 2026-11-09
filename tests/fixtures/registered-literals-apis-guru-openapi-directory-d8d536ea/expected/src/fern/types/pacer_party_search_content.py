

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pacer_case_search_content import PacerCaseSearchContent
from .pacer_party_search_content_pcl_jurisdiction_type import PacerPartySearchContentPclJurisdictionType


class PacerPartySearchContent(UniversalBaseModel):
    object: str = pydantic.Field()
    """
    Name of the object
    """

    pcl_case_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pclCaseId"),
        pydantic.Field(alias="pclCaseId", description="Sequentially generated number that identifies the case."),
    ]
    """
    Sequentially generated number that identifies the case.
    """

    pcl_case_number: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pclCaseNumber"),
        pydantic.Field(alias="pclCaseNumber", description="The sequence number of the case."),
    ]
    """
    The sequence number of the case.
    """

    pcl_case_number_full: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCaseNumberFull"),
        pydantic.Field(alias="pclCaseNumberFull", description="Case Number."),
    ] = None
    """
    Case Number.
    """

    pcl_case_office: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCaseOffice"),
        pydantic.Field(alias="pclCaseOffice", description="The divisional office in which the case was filed."),
    ] = None
    """
    The divisional office in which the case was filed.
    """

    pcl_case_title: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCaseTitle"),
        pydantic.Field(alias="pclCaseTitle", description="Title of the case."),
    ] = None
    """
    Title of the case.
    """

    pcl_case_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCaseType"),
        pydantic.Field(alias="pclCaseType", description="Code that identifies the type of case."),
    ] = None
    """
    Code that identifies the type of case.
    """

    pcl_case_year: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pclCaseYear"),
        pydantic.Field(
            alias="pclCaseYear", description="The year in which the case falls. Could be two or four digit."
        ),
    ]
    """
    The year in which the case falls. Could be two or four digit.
    """

    pcl_court_case: typing_extensions.Annotated[
        PacerCaseSearchContent, FieldMetadata(alias="pclCourtCase"), pydantic.Field(alias="pclCourtCase")
    ]
    pcl_court_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCourtId"),
        pydantic.Field(
            alias="pclCourtId",
            description="The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B",
        ),
    ] = None
    """
    The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B
    """

    pcl_date_filed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDateFiled"),
        pydantic.Field(alias="pclDateFiled", description="Filing date of the case."),
    ] = None
    """
    Filing date of the case.
    """

    pcl_first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclFirstName"),
        pydantic.Field(
            alias="pclFirstName", description="This parameter represents the first name of the case when it is present"
        ),
    ] = None
    """
    This parameter represents the first name of the case when it is present
    """

    pcl_generation: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclGeneration"),
        pydantic.Field(
            alias="pclGeneration", description="This parameter represents the generation of the case when it is present"
        ),
    ] = None
    """
    This parameter represents the generation of the case when it is present
    """

    pcl_jurisdiction_type: typing_extensions.Annotated[
        PacerPartySearchContentPclJurisdictionType,
        FieldMetadata(alias="pclJurisdictionType"),
        pydantic.Field(
            alias="pclJurisdictionType",
            description="Link to case in the case management/electronic case files (CM/ECF) system at the court.",
        ),
    ]
    """
    Link to case in the case management/electronic case files (CM/ECF) system at the court.
    """

    pcl_last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclLastName"),
        pydantic.Field(
            alias="pclLastName", description="This parameter represents the last name of the case when it is present"
        ),
    ] = None
    """
    This parameter represents the last name of the case when it is present
    """

    pcl_middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMiddleName"),
        pydantic.Field(
            alias="pclMiddleName",
            description="This parameter represents the middle name of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the middle name of the case when it is present
    """

    pcl_party_role: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclPartyRole"),
        pydantic.Field(
            alias="pclPartyRole", description="This parameter represents the party role of the case when it is present"
        ),
    ] = None
    """
    This parameter represents the party role of the case when it is present
    """

    pcl_party_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclPartyType"),
        pydantic.Field(
            alias="pclPartyType", description="This parameter represents the party type of the case when it is present"
        ),
    ] = None
    """
    This parameter represents the party type of the case when it is present
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
