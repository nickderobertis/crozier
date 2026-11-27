

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssemblySpecSharedConstructsItem(UniversalBaseModel):
    fragments: typing.List[str] = pydantic.Field()
    """
    Ordered list of fragment IDs to use in creating the construct, or a special option (SKIP) to indicate a bin should be skipped.
    """

    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
