

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetPatchSeismicmeta(UniversalBaseModel):
    """
    Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.
    """

    kind: typing.Optional[str] = None
    data: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
