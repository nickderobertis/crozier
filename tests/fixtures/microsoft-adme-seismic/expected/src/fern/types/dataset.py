

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataset_openzgy_v1 import DatasetOpenzgyV1
from .dataset_segy_v1 import DatasetSegyV1
from .dataset_seismicmeta import DatasetSeismicmeta


class Dataset(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the dataset.
    """

    tenant: str = pydantic.Field()
    """
    Name of the tenant.
    """

    subproject: str = pydantic.Field()
    """
    Name of the subproject.
    """

    path: str = pydantic.Field()
    """
    Path to the dataset inside a subproject.
    """

    created_by: str = pydantic.Field()
    """
    Creator of the dataset.
    """

    created_date: str = pydantic.Field()
    """
    Date when the dataset was created.
    """

    last_modified_date: str = pydantic.Field()
    """
    Date when the dataset was last modified.
    """

    filemetadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Number of objects and the size in bytes of the dataset.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Generic information stored as key,value pairs for the dataset.
    """

    gcsurl: str = pydantic.Field()
    """
    Cloud storage object identifier.
    """

    readonly: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the dataset is readonly.
    """

    ltag: typing.Optional[str] = pydantic.Field(default=None)
    """
    Legal tag associated with the dataset.
    """

    ctag: str = pydantic.Field()
    """
    The coherency tag associated with the dataset. (It changes every time the dataset is updated.)
    """

    seismicmeta_guid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Seismic storage record identifier.
    """

    sbit: typing.Optional[str] = pydantic.Field(default=None)
    """
    The session lockID.
    """

    sbit_count: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of sessions associated to the dataset.
    """

    seismicmeta: typing.Optional[DatasetSeismicmeta] = pydantic.Field(default=None)
    """
    Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.
    """

    openzgy_v1: typing.Optional[DatasetOpenzgyV1] = pydantic.Field(default=None)
    """
    The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.
    """

    segy_v1: typing.Optional[DatasetSegyV1] = pydantic.Field(default=None)
    """
    A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
