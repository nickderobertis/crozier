

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ColumnConfig(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Column-Config to be used when resolving with Upload.
    """

    label: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Map of Localized labels.
    """

    description: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Map of Localized descriptions.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of column in result csv.
    """

    pad: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pad-String when uploading data, to avoid problems with some tools truncating leading zeros or similar.
    """

    length: typing.Optional[int] = pydantic.Field(default=None)
    """
    In conjunction with pad, the length of the padded string.
    """

    resolvable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True, if the Column should be printed to output. This can be used to have resolvable but not printable fields in mapping.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
