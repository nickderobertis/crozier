

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact import Contact
from .judge_type import JudgeType
from .possible_norm_judge import PossibleNormJudge


class Judge(UniversalBaseModel):
    contact: Contact
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="When was the judge first fetched from the court site."),
    ]
    """
    When was the judge first fetched from the court site.
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name of the judge. This is normalized by UniCourt."),
    ] = None
    """
    First name of the judge. This is normalized by UniCourt.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible",
            description="Signifies if the judge as this judge type is currently isVisible or not for the case.",
        ),
    ]
    """
    Signifies if the judge as this judge type is currently isVisible or not for the case.
    """

    judge_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="judgeId"),
        pydantic.Field(
            alias="judgeId",
            description="ID for the judge in this case. This ID is unique within a case and NOT across cases. If the same Judge were to appear in another case this ID would be different.",
        ),
    ]
    """
    ID for the judge in this case. This ID is unique within a case and NOT across cases. If the same Judge were to appear in another case this ID would be different.
    """

    judge_type: typing_extensions.Annotated[
        typing.Optional[JudgeType], FieldMetadata(alias="judgeType"), pydantic.Field(alias="judgeType")
    ] = None
    last_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="When was the judge last fetched from the court site."),
    ]
    """
    When was the judge last fetched from the court site.
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name of the judge. This is normalized by UniCourt."),
    ] = None
    """
    Last name of the judge. This is normalized by UniCourt.
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Middle name of the judge. This is normalized by UniCourt."),
    ] = None
    """
    Middle name of the judge. This is normalized by UniCourt.
    """

    name: str = pydantic.Field()
    """
    Name of the judge as provided by Court.
    """

    name_prefix: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="namePrefix"), pydantic.Field(alias="namePrefix")
    ] = None
    name_suffix: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nameSuffix"), pydantic.Field(alias="nameSuffix")
    ] = None
    object: str = pydantic.Field()
    """
    Name of the object
    """

    possible_norm_judge_array: typing_extensions.Annotated[
        typing.List[typing.Optional[PossibleNormJudge]],
        FieldMetadata(alias="possibleNormJudgeArray"),
        pydantic.Field(alias="possibleNormJudgeArray"),
    ]
    source_judge_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceJudgeType"), pydantic.Field(alias="sourceJudgeType")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
