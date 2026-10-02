

import typing

CellOutputMimetype = typing.Union[
    typing.Literal[
        "application/json",
        "application/vnd.jupyter.widget-view+json",
        "application/vnd.marimo+error",
        "application/vnd.marimo+mimebundle",
        "application/vnd.marimo+traceback",
        "application/vnd.vega.v5+json",
        "application/vnd.vega.v6+json",
        "application/vnd.vegalite.v5+json",
        "application/vnd.vegalite.v6+json",
        "image/avif",
        "image/bmp",
        "image/gif",
        "image/jpeg",
        "image/png",
        "image/svg+xml",
        "image/tiff",
        "text/csv",
        "text/html",
        "text/latex",
        "text/markdown",
        "text/password",
        "text/plain",
        "video/mp4",
        "video/mpeg",
    ],
    typing.Any,
]
