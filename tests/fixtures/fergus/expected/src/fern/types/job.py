

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_active_quote import JobActiveQuote
from .job_customer import JobCustomer
from .job_main_contact import JobMainContact
from .job_site_address import JobSiteAddress
from .links import Links


class Job(UniversalBaseModel):
    id: float
    job_no: typing_extensions.Annotated[str, FieldMetadata(alias="jobNo"), pydantic.Field(alias="jobNo")]
    description: typing.Optional[str] = None
    long_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="longDescription"), pydantic.Field(alias="longDescription")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    job_type: typing_extensions.Annotated[str, FieldMetadata(alias="jobType"), pydantic.Field(alias="jobType")]
    status: str
    assigned_groups: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="assignedGroups"),
        pydantic.Field(
            alias="assignedGroups",
            description="Default group assigned to a job for easy tracking. This gets assigned automatically by default on new job phases.",
        ),
    ]
    """
    Default group assigned to a job for easy tracking. This gets assigned automatically by default on new job phases.
    """

    customer: typing.Optional[JobCustomer] = None
    site_address: typing_extensions.Annotated[
        typing.Optional[JobSiteAddress], FieldMetadata(alias="siteAddress"), pydantic.Field(alias="siteAddress")
    ] = None
    main_contact: typing_extensions.Annotated[
        typing.Optional[JobMainContact], FieldMetadata(alias="mainContact"), pydantic.Field(alias="mainContact")
    ] = None
    active_quote: typing_extensions.Annotated[
        typing.Optional[JobActiveQuote], FieldMetadata(alias="activeQuote"), pydantic.Field(alias="activeQuote")
    ] = None
    links: typing.List[Links]
    on_hold: typing_extensions.Annotated[bool, FieldMetadata(alias="onHold"), pydantic.Field(alias="onHold")]
    archived: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
