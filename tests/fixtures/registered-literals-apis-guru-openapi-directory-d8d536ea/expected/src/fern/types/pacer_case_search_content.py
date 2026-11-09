

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pacer_case_search_content_pcl_jurisdiction_type import PacerCaseSearchContentPclJurisdictionType


class PacerCaseSearchContent(UniversalBaseModel):
    object: str = pydantic.Field()
    """
    Name of the object
    """

    pcl_bankruptcy_chapter: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclBankruptcyChapter"),
        pydantic.Field(
            alias="pclBankruptcyChapter",
            description="This parameter represents the bankruptcy chapter of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the bankruptcy chapter of the case when it is present
    """

    pcl_case_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pclCaseId"),
        pydantic.Field(alias="pclCaseId", description="Sequentially generated number that identifies the case."),
    ]
    """
    Sequentially generated number that identifies the case.
    """

    pcl_case_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCaseLink"),
        pydantic.Field(
            alias="pclCaseLink",
            description="Link to case in the case management/electronic case files (CM/ECF) system at the court.",
        ),
    ] = None
    """
    Link to case in the case management/electronic case files (CM/ECF) system at the court.
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

    pcl_civil_cto_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilCtoNumber"),
        pydantic.Field(
            alias="pclCivilCtoNumber",
            description="This parameter represents the civil cto number of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil cto number of the case when it is present
    """

    pcl_civil_date_disposition: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilDateDisposition"),
        pydantic.Field(
            alias="pclCivilDateDisposition",
            description="This parameter represents the civil disposition date of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil disposition date of the case when it is present
    """

    pcl_civil_date_initiated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilDateInitiated"),
        pydantic.Field(
            alias="pclCivilDateInitiated",
            description="This parameter represents the civil initiated date of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil initiated date of the case when it is present
    """

    pcl_civil_date_terminated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilDateTerminated"),
        pydantic.Field(
            alias="pclCivilDateTerminated",
            description="This parameter represents the civil terminated date of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil terminated date of the case when it is present
    """

    pcl_civil_stat_disposition: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilStatDisposition"),
        pydantic.Field(
            alias="pclCivilStatDisposition",
            description="This parameter represents the civil stat disposition of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil stat disposition of the case when it is present
    """

    pcl_civil_stat_initiated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilStatInitiated"),
        pydantic.Field(
            alias="pclCivilStatInitiated",
            description="This parameter represents the civil stat initiated of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil stat initiated of the case when it is present
    """

    pcl_civil_stat_terminated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilStatTerminated"),
        pydantic.Field(
            alias="pclCivilStatTerminated",
            description="This parameter represents the civil stat terminated of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil stat terminated of the case when it is present
    """

    pcl_civil_transferee: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclCivilTransferee"),
        pydantic.Field(
            alias="pclCivilTransferee",
            description="This parameter represents the civil transferee of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the civil transferee of the case when it is present
    """

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

    pcl_date_discharged: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDateDischarged"),
        pydantic.Field(
            alias="pclDateDischarged",
            description="This parameter represents the date discharged of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the date discharged of the case when it is present
    """

    pcl_date_dismissed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDateDismissed"),
        pydantic.Field(
            alias="pclDateDismissed",
            description="This parameter represents the date dismissed of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the date dismissed of the case when it is present
    """

    pcl_date_filed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDateFiled"),
        pydantic.Field(alias="pclDateFiled", description="Filing date of the case."),
    ] = None
    """
    Filing date of the case.
    """

    pcl_date_reopened: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDateReopened"),
        pydantic.Field(
            alias="pclDateReopened",
            description="This parameter represents the date reopened of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the date reopened of the case when it is present
    """

    pcl_date_termed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDateTermed"),
        pydantic.Field(
            alias="pclDateTermed",
            description="This parameter represents the date termed of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the date termed of the case when it is present
    """

    pcl_disposition: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDisposition"),
        pydantic.Field(
            alias="pclDisposition",
            description="This parameter represents the disposition of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the disposition of the case when it is present
    """

    pcl_disposition_method: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclDispositionMethod"),
        pydantic.Field(
            alias="pclDispositionMethod",
            description="This parameter represents the disposition method of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the disposition method of the case when it is present
    """

    pcl_joint_bankruptcy_flag: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclJointBankruptcyFlag"),
        pydantic.Field(
            alias="pclJointBankruptcyFlag",
            description="This parameter represents the joint bankruptcy flag of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the joint bankruptcy flag of the case when it is present
    """

    pcl_joint_discharged_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclJointDischargedDate"),
        pydantic.Field(
            alias="pclJointDischargedDate",
            description="This parameter represents the joint discharged date of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the joint discharged date of the case when it is present
    """

    pcl_joint_dismissed_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclJointDismissedDate"),
        pydantic.Field(
            alias="pclJointDismissedDate",
            description="This parameter represents the joint dismissed date of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the joint dismissed date of the case when it is present
    """

    pcl_joint_disposition_method: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclJointDispositionMethod"),
        pydantic.Field(
            alias="pclJointDispositionMethod",
            description="This parameter represents the joint disposition method of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the joint disposition method of the case when it is present
    """

    pcl_jpml_number: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pclJpmlNumber"),
        pydantic.Field(alias="pclJpmlNumber", description="JPML Case Seed number."),
    ] = None
    """
    JPML Case Seed number.
    """

    pcl_jurisdiction_type: typing_extensions.Annotated[
        PacerCaseSearchContentPclJurisdictionType,
        FieldMetadata(alias="pclJurisdictionType"),
        pydantic.Field(
            alias="pclJurisdictionType",
            description="Link to case in the case management/electronic case files (CM/ECF) system at the court.",
        ),
    ]
    """
    Link to case in the case management/electronic case files (CM/ECF) system at the court.
    """

    pcl_mdl_court_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlCourtId"),
        pydantic.Field(alias="pclMdlCourtId", description="Which court does this mdl belongs too."),
    ] = None
    """
    Which court does this mdl belongs too.
    """

    pcl_mdl_date_ordered: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlDateOrdered"),
        pydantic.Field(
            alias="pclMdlDateOrdered",
            description="This parameter represents the mdl date ordered of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the mdl date ordered of the case when it is present
    """

    pcl_mdl_date_received: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlDateReceived"),
        pydantic.Field(
            alias="pclMdlDateReceived",
            description="This parameter represents the mdl date received of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the mdl date received of the case when it is present
    """

    pcl_mdl_extension: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlExtension"),
        pydantic.Field(
            alias="pclMdlExtension",
            description="This parameter represents the mdl extension of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the mdl extension of the case when it is present
    """

    pcl_mdl_judge_last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlJudgeLastName"),
        pydantic.Field(
            alias="pclMdlJudgeLastName",
            description="This parameter represents the mdl judge lastname of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the mdl judge lastname of the case when it is present
    """

    pcl_mdl_littype: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlLittype"),
        pydantic.Field(
            alias="pclMdlLittype",
            description="This parameter represents the mdl lit type of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the mdl lit type of the case when it is present
    """

    pcl_mdl_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlStatus"),
        pydantic.Field(
            alias="pclMdlStatus", description="This parameter represents the mdl status of the case when it is present"
        ),
    ] = None
    """
    This parameter represents the mdl status of the case when it is present
    """

    pcl_mdl_transferee: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlTransferee"),
        pydantic.Field(
            alias="pclMdlTransferee",
            description="This parameter represents the mdl transferee of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the mdl transferee of the case when it is present
    """

    pcl_mdl_transferee_district: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclMdlTransfereeDistrict"),
        pydantic.Field(
            alias="pclMdlTransfereeDistrict",
            description="This parameter represents the mdl transferee district of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the mdl transferee district of the case when it is present
    """

    pcl_nature_of_suit: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pclNatureOfSuit"),
        pydantic.Field(
            alias="pclNatureOfSuit",
            description="This parameter represents the nature of suit of the case when it is present",
        ),
    ] = None
    """
    This parameter represents the nature of suit of the case when it is present
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
