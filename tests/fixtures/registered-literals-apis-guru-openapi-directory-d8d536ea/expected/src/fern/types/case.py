

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attorneys import Attorneys
from .case_cause_of_action import CaseCauseOfAction
from .case_charge import CaseCharge
from .case_documents import CaseDocuments
from .case_source_data_status import CaseSourceDataStatus
from .case_stats import CaseStats
from .case_status import CaseStatus
from .case_type import CaseType
from .court import Court
from .court_location import CourtLocation
from .docket_entries import DocketEntries
from .hearings import Hearings
from .judges import Judges
from .parties import Parties
from .related_cases import RelatedCases
from .source_case_data import SourceCaseData


class Case(UniversalBaseModel):
    attorneys: typing.Optional[Attorneys] = None
    case_documents: typing_extensions.Annotated[
        typing.Optional[CaseDocuments], FieldMetadata(alias="caseDocuments"), pydantic.Field(alias="caseDocuments")
    ] = None
    case_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseId"), pydantic.Field(alias="caseId", description="Unique identifier of Case.")
    ]
    """
    Unique identifier of Case.
    """

    case_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="caseName"),
        pydantic.Field(alias="caseName", description="Case name as provided by Court."),
    ] = None
    """
    Case name as provided by Court.
    """

    case_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseNumber"),
        pydantic.Field(alias="caseNumber", description="Case number as provided by Court."),
    ]
    """
    Case number as provided by Court.
    """

    case_stats: typing_extensions.Annotated[
        CaseStats, FieldMetadata(alias="caseStats"), pydantic.Field(alias="caseStats")
    ]
    case_status: typing_extensions.Annotated[
        typing.Optional[CaseStatus], FieldMetadata(alias="caseStatus"), pydantic.Field(alias="caseStatus")
    ] = None
    case_type: typing_extensions.Annotated[
        typing.Optional[CaseType], FieldMetadata(alias="caseType"), pydantic.Field(alias="caseType")
    ] = None
    cause_of_action_array: typing_extensions.Annotated[
        typing.List[typing.Optional[CaseCauseOfAction]],
        FieldMetadata(alias="causeOfActionArray"),
        pydantic.Field(
            alias="causeOfActionArray", description="Array of cause of Actions that are added to this case."
        ),
    ]
    """
    Array of cause of Actions that are added to this case.
    """

    charge_array: typing_extensions.Annotated[
        typing.List[typing.Optional[CaseCharge]],
        FieldMetadata(alias="chargeArray"),
        pydantic.Field(alias="chargeArray", description="Array of charges that are added to this case."),
    ]
    """
    Array of charges that are added to this case.
    """

    court: typing.Optional[Court] = None
    court_location: typing_extensions.Annotated[
        typing.Optional[CourtLocation], FieldMetadata(alias="courtLocation"), pydantic.Field(alias="courtLocation")
    ] = None
    court_service_status_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="courtServiceStatusAPI"),
        pydantic.Field(alias="courtServiceStatusAPI", description="API to get the service statuses of the given case."),
    ] = None
    """
    API to get the service statuses of the given case.
    """

    court_service_status_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="courtServiceStatusId"),
        pydantic.Field(
            alias="courtServiceStatusId",
            description="Court Service Status ID of the requested case where we can use it to get the service status",
        ),
    ] = None
    """
    Court Service Status ID of the requested case where we can use it to get the service status
    """

    docket_entries: typing_extensions.Annotated[
        typing.Optional[DocketEntries], FieldMetadata(alias="docketEntries"), pydantic.Field(alias="docketEntries")
    ] = None
    export_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="exportAPI"),
        pydantic.Field(
            alias="exportAPI",
            description="When a case is beyond the threshold of entities we provide this link so that the user can request and get all the data of the case with one additional call. This data will be zipped and sent via a webhoook.",
        ),
    ]
    """
    When a case is beyond the threshold of entities we provide this link so that the user can request and get all the data of the case with one additional call. This data will be zipped and sent via a webhoook.
    """

    filed_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="filedDate"),
        pydantic.Field(
            alias="filedDate",
            description="Filing date for the case provided by the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz",
        ),
    ]
    """
    Filing date for the case provided by the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz
    """

    first_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(
            alias="firstFetchDate",
            description="The date and time when the case was first fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,.",
        ),
    ]
    """
    The date and time when the case was first fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,.
    """

    has_documents_with_preview: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasDocumentsWithPreview"),
        pydantic.Field(
            alias="hasDocumentsWithPreview",
            description="This field will be set to TRUE if atleast one document has a preview.",
        ),
    ]
    """
    This field will be set to TRUE if atleast one document has a preview.
    """

    has_only_meta_info: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasOnlyMetaInfo"),
        pydantic.Field(
            alias="hasOnlyMetaInfo",
            description="This field determines if this case object has only meta information. If the value is true and if the full information is required you would need to call the updateCase API.",
        ),
    ]
    """
    This field determines if this case object has only meta information. If the value is true and if the full information is required you would need to call the updateCase API.
    """

    hearings: typing.Optional[Hearings] = None
    judges: typing.Optional[Judges] = None
    last_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(
            alias="lastFetchDate",
            description="The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist.",
        ),
    ]
    """
    The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist.
    """

    last_fetch_date_with_updates: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDateWithUpdates"),
        pydantic.Field(
            alias="lastFetchDateWithUpdates",
            description="The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,",
        ),
    ]
    """
    The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    participants_last_fetch_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="participantsLastFetchDate"),
        pydantic.Field(
            alias="participantsLastFetchDate",
            description="The date and time when parties/attorneys were last updated from the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: This is currently applicable for Federal PACER cases since we have an option to exclude parties and fetch only latest docket entries when updating cases to save PACER fees.",
        ),
    ] = None
    """
    The date and time when parties/attorneys were last updated from the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: This is currently applicable for Federal PACER cases since we have an option to exclude parties and fetch only latest docket entries when updating cases to save PACER fees.
    """

    parties: typing.Optional[Parties] = None
    related_cases: typing_extensions.Annotated[
        typing.Optional[RelatedCases], FieldMetadata(alias="relatedCases"), pydantic.Field(alias="relatedCases")
    ] = None
    source_case_data: typing_extensions.Annotated[
        SourceCaseData, FieldMetadata(alias="sourceCaseData"), pydantic.Field(alias="sourceCaseData")
    ]
    source_data_status: typing_extensions.Annotated[
        typing.Optional[CaseSourceDataStatus],
        FieldMetadata(alias="sourceDataStatus"),
        pydantic.Field(
            alias="sourceDataStatus",
            description="The status of source data of case. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Case has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site.",
        ),
    ] = None
    """
    The status of source data of case. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Case has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to the case page in UniCourt Application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
