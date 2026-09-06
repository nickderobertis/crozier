

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewViewType(enum.StrEnum):
    """
    Type of object that the view corresponds to.
    """

    PROJECTS = "projects"
    EXPERIMENTS = "experiments"
    EXPERIMENT = "experiment"
    PLAYGROUNDS = "playgrounds"
    PLAYGROUND = "playground"
    DATASETS = "datasets"
    DATASET = "dataset"
    PROMPTS = "prompts"
    PARAMETERS = "parameters"
    TOOLS = "tools"
    SCORERS = "scorers"
    CLASSIFIERS = "classifiers"
    LOGS = "logs"
    MONITOR = "monitor"
    FOR_REVIEW_PROJECT_LOG = "for_review_project_log"
    FOR_REVIEW_EXPERIMENTS = "for_review_experiments"
    FOR_REVIEW_DATASETS = "for_review_datasets"

    def visit(
        self,
        projects: typing.Callable[[], T_Result],
        experiments: typing.Callable[[], T_Result],
        experiment: typing.Callable[[], T_Result],
        playgrounds: typing.Callable[[], T_Result],
        playground: typing.Callable[[], T_Result],
        datasets: typing.Callable[[], T_Result],
        dataset: typing.Callable[[], T_Result],
        prompts: typing.Callable[[], T_Result],
        parameters: typing.Callable[[], T_Result],
        tools: typing.Callable[[], T_Result],
        scorers: typing.Callable[[], T_Result],
        classifiers: typing.Callable[[], T_Result],
        logs: typing.Callable[[], T_Result],
        monitor: typing.Callable[[], T_Result],
        for_review_project_log: typing.Callable[[], T_Result],
        for_review_experiments: typing.Callable[[], T_Result],
        for_review_datasets: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ViewViewType.PROJECTS:
            return projects()
        if self is ViewViewType.EXPERIMENTS:
            return experiments()
        if self is ViewViewType.EXPERIMENT:
            return experiment()
        if self is ViewViewType.PLAYGROUNDS:
            return playgrounds()
        if self is ViewViewType.PLAYGROUND:
            return playground()
        if self is ViewViewType.DATASETS:
            return datasets()
        if self is ViewViewType.DATASET:
            return dataset()
        if self is ViewViewType.PROMPTS:
            return prompts()
        if self is ViewViewType.PARAMETERS:
            return parameters()
        if self is ViewViewType.TOOLS:
            return tools()
        if self is ViewViewType.SCORERS:
            return scorers()
        if self is ViewViewType.CLASSIFIERS:
            return classifiers()
        if self is ViewViewType.LOGS:
            return logs()
        if self is ViewViewType.MONITOR:
            return monitor()
        if self is ViewViewType.FOR_REVIEW_PROJECT_LOG:
            return for_review_project_log()
        if self is ViewViewType.FOR_REVIEW_EXPERIMENTS:
            return for_review_experiments()
        if self is ViewViewType.FOR_REVIEW_DATASETS:
            return for_review_datasets()
