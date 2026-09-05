

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetSnapshot(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the dataset snapshot
    """

    dataset_id: str = pydantic.Field()
    """
    Unique identifier for the dataset that this snapshot belongs to
    """

    name: str = pydantic.Field()
    """
    Name of the dataset snapshot
    """

    description: typing.Optional[str] = None
    xact_id: str = pydantic.Field()
    """
    Transaction id of the brainstore version at the time of the snapshot
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of dataset snapshot creation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
