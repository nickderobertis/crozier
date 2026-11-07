

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesAddonReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the node addon entity.
    """

    configured: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this node has been configured with an addon folder.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this node has a NodeSettings object associated with it.
    """

    external_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the associated node addon account, if any.
    """

    folder_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the linked folder from the addon provider.
    """

    folder_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The folder path of the linked folder from the addon provider. Google Drive specific
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    A label specific to the addon provider.
    """

    node_has_auth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this node is fully authorized to use this node addon.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    An external link specific to the addon provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
