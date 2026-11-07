

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .string import String


class ReportCheck(UniversalBaseModel):
    """
    report on checking contents of chunks
    """

    result: typing.Optional[str] = pydantic.Field(default=None)
    """
    the result of the check
    """

    visited_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="visitedCnt"),
        pydantic.Field(alias="visitedCnt", description="the number of visited items in the cache"),
    ] = None
    """
    the number of visited items in the cache
    """

    checked_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="checkedCnt"),
        pydantic.Field(alias="checkedCnt", description="the number of checks"),
    ] = None
    """
    the number of checks
    """

    skipped_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="skippedCnt"),
        pydantic.Field(alias="skippedCnt", description="the number of skipped checks"),
    ] = None
    """
    the number of skipped checks
    """

    passed_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="passedCnt"),
        pydantic.Field(alias="passedCnt", description="the number of passed checks"),
    ] = None
    """
    the number of passed checks
    """

    failed_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="failedCnt"),
        pydantic.Field(alias="failedCnt", description="the number of failed checks"),
    ] = None
    """
    the number of failed checks
    """

    msg_strings: typing_extensions.Annotated[
        typing.Optional[typing.List[String]],
        FieldMetadata(alias="msgStrings"),
        pydantic.Field(alias="msgStrings", description="an array of messages explaining failed checks"),
    ] = None
    """
    an array of messages explaining failed checks
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    the reason for the test
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
