

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_ref import ImageRef


class MappingRule(UniversalBaseModel):
    id: typing.Optional[str] = None
    image: ImageRef
    name: str
    policy_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional single policy to evalute, if set will override any value in policy_ids, for backwards compatibility. Generally, policy_ids should be used even with a array of length 1.
    """

    policy_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of policyIds to evaluate in order, to completion
    """

    registry: str
    repository: str
    whitelist_ids: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
