

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_selection_rule import ImageSelectionRule
from .mapping_rule import MappingRule
from .policy import Policy
from .whitelist import Whitelist


class PolicyBundle(UniversalBaseModel):
    """
    A bundle containing a set of policies, whitelists, and rules for mapping them to specific images
    """

    blacklisted_images: typing.Optional[typing.List[ImageSelectionRule]] = pydantic.Field(default=None)
    """
    List of mapping rules that define which images should always result in a STOP/FAIL policy result regardless of policy content or presence in whitelisted_images
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the bundle, human readable
    """

    id: str = pydantic.Field()
    """
    Id of the bundle
    """

    mappings: typing.List[MappingRule] = pydantic.Field()
    """
    Mapping rules for defining which policy and whitelist(s) to apply to an image based on a match of the image tag or id. Evaluated in order.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human readable name for the bundle
    """

    policies: typing.List[Policy] = pydantic.Field()
    """
    Policies which define the go/stop/warn status of an image using rule matches on image properties
    """

    version: str = pydantic.Field()
    """
    Version id for this bundle format
    """

    whitelisted_images: typing.Optional[typing.List[ImageSelectionRule]] = pydantic.Field(default=None)
    """
    List of mapping rules that define which images should always be passed (unless also on the blacklist), regardless of policy result.
    """

    whitelists: typing.Optional[typing.List[Whitelist]] = pydantic.Field(default=None)
    """
    Whitelists which define which policy matches to disregard explicitly in the final policy decision
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
