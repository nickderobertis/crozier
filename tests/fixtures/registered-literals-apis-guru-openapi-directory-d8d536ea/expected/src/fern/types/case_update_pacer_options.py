

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_update_pacer_options_additional_page_array_item import CaseUpdatePacerOptionsAdditionalPageArrayItem
from .case_update_pacer_options_refresh_type import CaseUpdatePacerOptionsRefreshType


class CaseUpdatePacerOptions(UniversalBaseModel):
    """
    Applicable for PACER cases.
    """

    additional_page_array: typing_extensions.Annotated[
        typing.Optional[typing.List[CaseUpdatePacerOptionsAdditionalPageArrayItem]],
        FieldMetadata(alias="additionalPageArray"),
        pydantic.Field(
            alias="additionalPageArray",
            description='Currently this option is only applicable for Federal PACER cases. The default behavior of the Case Update is to fetch the Docket Report from PACER which includes the parties and attorneys too.\n\nHowever if you need to fetch information for other pages in PACER you will need to specify it here.\n- associatedCases:\n> This will fetch the Associated Cases page in PACER if available. This page consists of related cases especially applicable for Multi-District Litigation cases and Member Cases. Including this option will internally link all related cases in our system. Data from this page will be available via the Related Cases API.\n- caseSummary:\n> This will fetch the Case Summary page in PACER if available. This page consists of additional case info which is not present in the Docket Report page. Data from this page will be structured and available as response in the Case API’s ```additional_info``` field.\n- listOfCreditors:\n> This page will fetch the “List Of Creditors” page for PACER Bankruptcy cases of case type "bk". Note that this page cannot be extracted for Bankruptcy cases of case type "ap" (Adversary Proceedings). This page consists of the Creditor information like the name and address of the Creditors. Data from this page will be structured and available as response in the Case API.',
        ),
    ] = None
    """
    Currently this option is only applicable for Federal PACER cases. The default behavior of the Case Update is to fetch the Docket Report from PACER which includes the parties and attorneys too.
    
    However if you need to fetch information for other pages in PACER you will need to specify it here.
    - associatedCases:
    > This will fetch the Associated Cases page in PACER if available. This page consists of related cases especially applicable for Multi-District Litigation cases and Member Cases. Including this option will internally link all related cases in our system. Data from this page will be available via the Related Cases API.
    - caseSummary:
    > This will fetch the Case Summary page in PACER if available. This page consists of additional case info which is not present in the Docket Report page. Data from this page will be structured and available as response in the Case API’s ```additional_info``` field.
    - listOfCreditors:
    > This page will fetch the “List Of Creditors” page for PACER Bankruptcy cases of case type "bk". Note that this page cannot be extracted for Bankruptcy cases of case type "ap" (Adversary Proceedings). This page consists of the Creditor information like the name and address of the Creditors. Data from this page will be structured and available as response in the Case API.
    """

    fetch_participants_if_older_than_days: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="fetchParticipantsIfOlderThanDays"),
        pydantic.Field(
            alias="fetchParticipantsIfOlderThanDays",
            description="**Currently this option is only applicable for Federal PACER cases. You can limit how often parties and attorneys for a PACER case are fetched to reduce your PACER fees. If you are tracking cases daily or hourly you could easily end up with a large PACER bill.**\n\n**Use Case: Cases are typically updated to check for new docket entry filings. However every update to PACER case costs money. Participants for a case change less often than docket entry filings. So fetching participants for every update might result in unnecessary PACER costs; especially on cases which have a lot of parties and attorneys. So instead of getting charged the minimum cost of $0.10 for an update which might have had few docket entries, you could end up spending $3 for every update because there were a lot of parties for that case that were also fetched.**\n\n**With this option you can choose when to fetch parties for case based on when was it last fetched.**\nYou can limit how often this participants are fetched in a PACER case to keep your PACER costs under control.\n\nMin days is 0 and Max days is 100.\n\nExample:\n1.  Specifying a value of 0 ensures that participants are fetched from PACER for this case update irrespective of when the participants were last fetched.\n2.  Specifying a value of 30 ensures that participants are fetched from PACER for this case update only if the last fetch was older than 30 days.",
        ),
    ] = None
    """
    **Currently this option is only applicable for Federal PACER cases. You can limit how often parties and attorneys for a PACER case are fetched to reduce your PACER fees. If you are tracking cases daily or hourly you could easily end up with a large PACER bill.**
    
    **Use Case: Cases are typically updated to check for new docket entry filings. However every update to PACER case costs money. Participants for a case change less often than docket entry filings. So fetching participants for every update might result in unnecessary PACER costs; especially on cases which have a lot of parties and attorneys. So instead of getting charged the minimum cost of $0.10 for an update which might have had few docket entries, you could end up spending $3 for every update because there were a lot of parties for that case that were also fetched.**
    
    **With this option you can choose when to fetch parties for case based on when was it last fetched.**
    You can limit how often this participants are fetched in a PACER case to keep your PACER costs under control.
    
    Min days is 0 and Max days is 100.
    
    Example:
    1.  Specifying a value of 0 ensures that participants are fetched from PACER for this case update irrespective of when the participants were last fetched.
    2.  Specifying a value of 30 ensures that participants are fetched from PACER for this case update only if the last fetch was older than 30 days.
    """

    pacer_client_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pacerClientCode"),
        pydantic.Field(
            alias="pacerClientCode",
            description="PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.",
        ),
    ] = None
    """
    PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.
    """

    pacer_user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pacerUserId"),
        pydantic.Field(
            alias="pacerUserId",
            description="**Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.**",
        ),
    ]
    """
    **Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.**
    """

    refresh_type: typing_extensions.Annotated[
        typing.Optional[CaseUpdatePacerOptionsRefreshType],
        FieldMetadata(alias="refreshType"),
        pydantic.Field(
            alias="refreshType",
            description="This flag determines whether to pull only new or pull all the docket entries for a PACER case being requested.\n\nOnly one of the two values is allowed:\n-   fetchNewDocketEntries:\n    >   Updates the PACER case with only new docket entries that have been added after the previous update of the case being requested.\n-   fetchAllDocketEntries:\n    >   Updates the PACER case by re-parsing all dockets from #1 till latest docket entry available.",
        ),
    ] = None
    """
    This flag determines whether to pull only new or pull all the docket entries for a PACER case being requested.
    
    Only one of the two values is allowed:
    -   fetchNewDocketEntries:
        >   Updates the PACER case with only new docket entries that have been added after the previous update of the case being requested.
    -   fetchAllDocketEntries:
        >   Updates the PACER case by re-parsing all dockets from #1 till latest docket entry available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
