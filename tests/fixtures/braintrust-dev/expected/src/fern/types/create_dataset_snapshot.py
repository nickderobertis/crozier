

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateDatasetSnapshot(UniversalBaseModel):
    dataset_id: str = pydantic.Field()
    """
    Unique identifier for the dataset that this snapshot belongs to
    """

    name: str = pydantic.Field()
    """
    Name of the dataset snapshot
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the dataset snapshot
    """

    xact_id: str = pydantic.Field()
    """
    Transaction id of the brainstore version at the time of the snapshot
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
