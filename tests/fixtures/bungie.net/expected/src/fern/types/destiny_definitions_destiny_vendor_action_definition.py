

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorActionDefinition(UniversalBaseModel):
    """
    If a vendor can ever end up performing actions, these are the properties that will be related to those actions. I'm not going to bother documenting this yet, as it is unused and unclear if it will ever be used... but in case it is ever populated and someone finds it useful, it is defined here.
    """

    action_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="actionHash")] = None
    action_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="actionId")] = None
    auto_perform_action: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="autoPerformAction")
    ] = None
    description: typing.Optional[str] = None
    execute_seconds: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="executeSeconds")] = None
    icon: typing.Optional[str] = None
    is_positive: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isPositive")] = None
    name: typing.Optional[str] = None
    verb: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
