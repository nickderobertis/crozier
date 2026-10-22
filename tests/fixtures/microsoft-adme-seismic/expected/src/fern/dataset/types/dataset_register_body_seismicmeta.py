

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataset_register_body_seismicmeta_data import DatasetRegisterBodySeismicmetaData


class DatasetRegisterBodySeismicmeta(UniversalBaseModel):
    """
    Seismic metadata to be stored as dataecosystem storage record.
    """

    kind: typing.Optional[str] = None
    data: typing.Optional[DatasetRegisterBodySeismicmetaData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
