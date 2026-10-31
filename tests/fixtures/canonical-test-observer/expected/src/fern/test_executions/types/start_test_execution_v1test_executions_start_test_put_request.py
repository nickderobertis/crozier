

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.charm_stage import CharmStage
from ...types.image_stage import ImageStage
from ...types.snap_stage import SnapStage
from ...types.solution_stage import SolutionStage
from ...types.start_deb_test_execution_request_execution_stage import StartDebTestExecutionRequestExecutionStage
from ...types.test_execution_relevant_link_create import TestExecutionRelevantLinkCreate
from ...types.test_execution_status import TestExecutionStatus


class StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap(UniversalBaseModel):
    family: typing.Literal["snap"] = "snap"
    name: str
    version: str
    arch: str
    environment: str
    expected_environments: typing.Optional[typing.List[str]] = None
    ci_link: typing.Optional[str] = None
    test_plan: str
    initial_status: typing.Optional[TestExecutionStatus] = None
    relevant_links: typing.Optional[typing.List[TestExecutionRelevantLinkCreate]] = None
    needs_assignment: typing.Optional[bool] = None
    revision: int
    track: str
    store: str
    branch: typing.Optional[str] = None
    execution_stage: SnapStage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StartTestExecutionV1TestExecutionsStartTestPutRequest_Deb(UniversalBaseModel):
    family: typing.Literal["deb"] = "deb"
    name: str
    version: str
    arch: str
    environment: str
    expected_environments: typing.Optional[typing.List[str]] = None
    ci_link: typing.Optional[str] = None
    test_plan: str
    initial_status: typing.Optional[TestExecutionStatus] = None
    relevant_links: typing.Optional[typing.List[TestExecutionRelevantLinkCreate]] = None
    needs_assignment: typing.Optional[bool] = None
    series: str
    repo: str
    source: typing.Optional[str] = None
    execution_stage: typing.Optional[StartDebTestExecutionRequestExecutionStage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StartTestExecutionV1TestExecutionsStartTestPutRequest_Charm(UniversalBaseModel):
    family: typing.Literal["charm"] = "charm"
    name: str
    version: str
    arch: str
    environment: str
    expected_environments: typing.Optional[typing.List[str]] = None
    ci_link: typing.Optional[str] = None
    test_plan: str
    initial_status: typing.Optional[TestExecutionStatus] = None
    relevant_links: typing.Optional[typing.List[TestExecutionRelevantLinkCreate]] = None
    needs_assignment: typing.Optional[bool] = None
    revision: int
    track: str
    branch: typing.Optional[str] = None
    execution_stage: CharmStage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StartTestExecutionV1TestExecutionsStartTestPutRequest_Image(UniversalBaseModel):
    family: typing.Literal["image"] = "image"
    name: typing.Optional[str] = None
    version: typing.Optional[str] = None
    arch: typing.Optional[str] = None
    environment: str
    expected_environments: typing.Optional[typing.List[str]] = None
    ci_link: typing.Optional[str] = None
    test_plan: str
    initial_status: typing.Optional[TestExecutionStatus] = None
    relevant_links: typing.Optional[typing.List[TestExecutionRelevantLinkCreate]] = None
    needs_assignment: typing.Optional[bool] = None
    execution_stage: typing.Optional[ImageStage] = None
    os: typing.Optional[str] = None
    release: typing.Optional[str] = None
    sha256: str
    owner: typing.Optional[str] = None
    image_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StartTestExecutionV1TestExecutionsStartTestPutRequest_Solution(UniversalBaseModel):
    family: typing.Literal["solution"] = "solution"
    name: str
    version: str
    arch: str
    environment: str
    expected_environments: typing.Optional[typing.List[str]] = None
    ci_link: typing.Optional[str] = None
    test_plan: str
    initial_status: typing.Optional[TestExecutionStatus] = None
    relevant_links: typing.Optional[typing.List[TestExecutionRelevantLinkCreate]] = None
    needs_assignment: typing.Optional[bool] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None
    execution_stage: SolutionStage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StartTestExecutionV1TestExecutionsStartTestPutRequest = typing_extensions.Annotated[
    typing.Union[
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Deb,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Charm,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Image,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Solution,
    ],
    pydantic.Field(discriminator="family"),
]
