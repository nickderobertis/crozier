

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact import Contact
from .norm_judge_public_data_aba_ratings import NormJudgePublicDataAbaRatings
from .norm_judge_public_data_bio import NormJudgePublicDataBio
from .norm_judge_public_data_education_array_item import NormJudgePublicDataEducationArrayItem
from .norm_judge_public_data_judicial_source import NormJudgePublicDataJudicialSource
from .norm_judge_public_data_name_history_array_item import NormJudgePublicDataNameHistoryArrayItem
from .service_history import ServiceHistory


class NormJudgePublicData(UniversalBaseModel):
    """
    This contains the Judge Public details that is obtained from various sources.
    """

    aba_ratings: typing_extensions.Annotated[
        typing.Optional[NormJudgePublicDataAbaRatings],
        FieldMetadata(alias="abaRatings"),
        pydantic.Field(alias="abaRatings", description="American Bar Association (ABA) Rating of the Judge."),
    ] = None
    """
    American Bar Association (ABA) Rating of the Judge.
    """

    alias_array: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="aliasArray"),
        pydantic.Field(alias="aliasArray", description="Other Names of the Judge."),
    ]
    """
    Other Names of the Judge.
    """

    bio: NormJudgePublicDataBio
    contact: Contact
    education_array: typing_extensions.Annotated[
        typing.List[NormJudgePublicDataEducationArrayItem],
        FieldMetadata(alias="educationArray"),
        pydantic.Field(alias="educationArray", description="The Education History of the judge."),
    ]
    """
    The Education History of the judge.
    """

    first_fetch_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="firstFetchDate"), pydantic.Field(alias="firstFetchDate")
    ] = None
    judicial_source: typing_extensions.Annotated[
        NormJudgePublicDataJudicialSource,
        FieldMetadata(alias="judicialSource"),
        pydantic.Field(alias="judicialSource", description="The judicial source of the Judge"),
    ]
    """
    The judicial source of the Judge
    """

    judicial_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="judicialStatus"),
        pydantic.Field(alias="judicialStatus", description="The judicial status of the Judge"),
    ] = None
    """
    The judicial status of the Judge
    """

    last_fetch_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastFetchDate"), pydantic.Field(alias="lastFetchDate")
    ] = None
    last_fetch_date_with_updates: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastFetchDateWithUpdates"),
        pydantic.Field(alias="lastFetchDateWithUpdates", description="Last Fetch Date of the Judge Update."),
    ] = None
    """
    Last Fetch Date of the Judge Update.
    """

    name_history_array: typing_extensions.Annotated[
        typing.List[NormJudgePublicDataNameHistoryArrayItem],
        FieldMetadata(alias="nameHistoryArray"),
        pydantic.Field(
            alias="nameHistoryArray",
            description="Name changes of the Judge. Change in the official name. Other names go to Alias array.",
        ),
    ]
    """
    Name changes of the Judge. Change in the official name. Other names go to Alias array.
    """

    object: str
    professional_career_array: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="professionalCareerArray"),
        pydantic.Field(alias="professionalCareerArray", description="The non-judicial career history of the judge."),
    ]
    """
    The non-judicial career history of the judge.
    """

    service_history_array: typing_extensions.Annotated[
        typing.List[ServiceHistory],
        FieldMetadata(alias="serviceHistoryArray"),
        pydantic.Field(alias="serviceHistoryArray", description="Judicial History of the Judge."),
    ]
    """
    Judicial History of the Judge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
