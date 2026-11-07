

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Email(UniversalBaseModel):
    """
    Email object data schema.
    """

    email_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="emailId"), pydantic.Field(alias="emailId", description="email id")
    ]
    """
    email id
    """

    first_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="Date at which this record is created in UniCourt."),
    ]
    """
    Date at which this record is created in UniCourt.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(alias="isVisible", description="Boolean indicating if the email is visible or not."),
    ]
    """
    Boolean indicating if the email is visible or not.
    """

    last_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="Date at which this record was updated in UniCourt."),
    ]
    """
    Date at which this record was updated in UniCourt.
    """

    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
