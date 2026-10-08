

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReportResponseJobsItem(UniversalBaseModel):
    jobid: typing.Optional[str] = pydantic.Field(default=None)
    """
    SMS ID
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Recipient phone number
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    SMS status
    """

    operator: typing.Optional[int] = pydantic.Field(default=None)
    """
    Operator code
    """

    msglen: typing.Optional[int] = pydantic.Field(default=None)
    """
    Message length
    """

    delivered_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deliveredDate"),
        pydantic.Field(alias="deliveredDate", description="Delivery date"),
    ] = None
    """
    Delivery date
    """

    error_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="errorCode"),
        pydantic.Field(alias="errorCode", description="Error code"),
    ] = None
    """
    Error code
    """

    referans_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="referansID"),
        pydantic.Field(alias="referansID", description="Reference ID"),
    ] = None
    """
    Reference ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
