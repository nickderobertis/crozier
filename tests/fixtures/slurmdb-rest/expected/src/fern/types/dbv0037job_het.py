

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobHet(UniversalBaseModel):
    """
    Heterogeneous Job details (optional)
    """

    job_id: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Parent HetJob id
    """

    job_offset: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Offset of this job to parent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
