

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetAndDirectories(UniversalBaseModel):
    datasets: typing.List[str] = pydantic.Field()
    """
    Array of datasets inside the subproject.
    """

    directories: typing.List[str] = pydantic.Field()
    """
    Array of directories inside the subproject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
