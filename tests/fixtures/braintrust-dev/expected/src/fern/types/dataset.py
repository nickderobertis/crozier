

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dataset(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the dataset
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the dataset belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the dataset. Within a project, dataset names are unique
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the dataset
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of dataset creation
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of dataset deletion, or null if the dataset is still active
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the dataset
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tags for the dataset
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User-controlled metadata about the dataset
    """

    url_slug: str = pydantic.Field()
    """
    URL slug for the dataset. used to construct dataset URLs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
