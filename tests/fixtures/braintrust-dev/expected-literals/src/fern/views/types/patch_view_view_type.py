

import typing

PatchViewViewType = typing.Union[
    typing.Literal[
        "projects",
        "experiments",
        "experiment",
        "playgrounds",
        "playground",
        "datasets",
        "dataset",
        "prompts",
        "parameters",
        "tools",
        "scorers",
        "classifiers",
        "logs",
        "monitor",
        "for_review_project_log",
        "for_review_experiments",
        "for_review_datasets",
    ],
    typing.Any,
]
