

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProvisioningApiAppInfo(UniversalBaseModel):
    active: typing.Optional[bool] = None
    activity: typing.Optional[typing.Dict[str, typing.Any]] = None
    author: typing.Optional[typing.Dict[str, typing.Any]] = None
    background_jobs: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="background-jobs"),
        pydantic.Field(alias="background-jobs"),
    ] = None
    bugs: typing.Optional[typing.Dict[str, typing.Any]] = None
    category: typing.Optional[typing.Dict[str, typing.Any]] = None
    collaboration: typing.Optional[typing.Dict[str, typing.Any]] = None
    commands: typing.Optional[typing.Dict[str, typing.Any]] = None
    default_enable: typing.Optional[typing.Dict[str, typing.Any]] = None
    dependencies: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: str
    discussion: typing.Optional[typing.Dict[str, typing.Any]] = None
    documentation: typing.Optional[typing.Dict[str, typing.Any]] = None
    groups: typing.Optional[typing.Dict[str, typing.Any]] = None
    id: str
    info: typing.Optional[typing.Dict[str, typing.Any]] = None
    internal: typing.Optional[bool] = None
    level: typing.Optional[int] = None
    licence: typing.Optional[typing.Dict[str, typing.Any]] = None
    name: str
    namespace: typing.Optional[typing.Dict[str, typing.Any]] = None
    navigations: typing.Optional[typing.Dict[str, typing.Any]] = None
    preview: typing.Optional[typing.Dict[str, typing.Any]] = None
    preview_as_icon: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="previewAsIcon"), pydantic.Field(alias="previewAsIcon")
    ] = None
    public: typing.Optional[typing.Dict[str, typing.Any]] = None
    remote: typing.Optional[typing.Dict[str, typing.Any]] = None
    removable: typing.Optional[bool] = None
    repair_steps: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="repair-steps"),
        pydantic.Field(alias="repair-steps"),
    ] = None
    repository: typing.Optional[typing.Dict[str, typing.Any]] = None
    sabre: typing.Optional[typing.Dict[str, typing.Any]] = None
    screenshot: typing.Optional[typing.Dict[str, typing.Any]] = None
    settings: typing.Optional[typing.Dict[str, typing.Any]] = None
    summary: str
    trash: typing.Optional[typing.Dict[str, typing.Any]] = None
    two_factor_providers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="two-factor-providers"),
        pydantic.Field(alias="two-factor-providers"),
    ] = None
    types: typing.Optional[typing.Dict[str, typing.Any]] = None
    version: str
    versions: typing.Optional[typing.Dict[str, typing.Any]] = None
    website: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
