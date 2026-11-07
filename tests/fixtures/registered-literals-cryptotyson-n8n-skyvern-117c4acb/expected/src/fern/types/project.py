

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Project(UniversalBaseModel):
    project_revision_id: str = pydantic.Field()
    """
    Unique identifier for this specific project revision
    """

    project_id: str = pydantic.Field()
    """
    User-facing project identifier, consistent across versions
    """

    organization_id: str = pydantic.Field()
    """
    ID of the organization that owns this project
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the workflow run or task run that generated this project
    """

    version: int = pydantic.Field()
    """
    Version number of the project
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp when the project was created
    """

    modified_at: dt.datetime = pydantic.Field()
    """
    Timestamp when the project was last modified
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the project was soft deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
