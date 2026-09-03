

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .check_result_status import CheckResultStatus


class CheckResult(UniversalBaseModel):
    status: typing.Optional[CheckResultStatus] = None
    score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Risk Score (0-1)
    """

    details: typing.Optional[str] = None
    last_checked: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastChecked"), pydantic.Field(alias="lastChecked")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
