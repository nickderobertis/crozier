

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExportRealmResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the data export created.
    
    **Changes**: New in Zulip 7.0 (feature level 182).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
