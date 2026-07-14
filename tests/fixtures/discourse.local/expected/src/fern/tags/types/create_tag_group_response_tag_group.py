

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateTagGroupResponseTagGroup(UniversalBaseModel):
    id: int
    name: str
    one_per_topic: bool
    parent_tag_name: typing.List[typing.Optional[typing.Any]]
    permissions: typing.Dict[str, typing.Optional[typing.Any]]
    tag_names: typing.List[typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
