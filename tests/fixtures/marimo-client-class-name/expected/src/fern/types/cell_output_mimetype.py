

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CellOutputMimetype(enum.StrEnum):
    APPLICATION_JSON = "application/json"
    APPLICATION_VND_JUPYTER_WIDGET_VIEW_JSON = "application/vnd.jupyter.widget-view+json"
    APPLICATION_VND_MARIMO_ERROR = "application/vnd.marimo+error"
    APPLICATION_VND_MARIMO_MIMEBUNDLE = "application/vnd.marimo+mimebundle"
    APPLICATION_VND_MARIMO_TRACEBACK = "application/vnd.marimo+traceback"
    APPLICATION_VND_VEGA_V5JSON = "application/vnd.vega.v5+json"
    APPLICATION_VND_VEGA_V6JSON = "application/vnd.vega.v6+json"
    APPLICATION_VND_VEGALITE_V5JSON = "application/vnd.vegalite.v5+json"
    APPLICATION_VND_VEGALITE_V6JSON = "application/vnd.vegalite.v6+json"
    IMAGE_AVIF = "image/avif"
    IMAGE_BMP = "image/bmp"
    IMAGE_GIF = "image/gif"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_SVG_XML = "image/svg+xml"
    IMAGE_TIFF = "image/tiff"
    TEXT_CSV = "text/csv"
    TEXT_HTML = "text/html"
    TEXT_LATEX = "text/latex"
    TEXT_MARKDOWN = "text/markdown"
    TEXT_PASSWORD = "text/password"
    TEXT_PLAIN = "text/plain"
    VIDEO_MP4 = "video/mp4"
    VIDEO_MPEG = "video/mpeg"

    def visit(
        self,
        application_json: typing.Callable[[], T_Result],
        application_vnd_jupyter_widget_view_json: typing.Callable[[], T_Result],
        application_vnd_marimo_error: typing.Callable[[], T_Result],
        application_vnd_marimo_mimebundle: typing.Callable[[], T_Result],
        application_vnd_marimo_traceback: typing.Callable[[], T_Result],
        application_vnd_vega_v5json: typing.Callable[[], T_Result],
        application_vnd_vega_v6json: typing.Callable[[], T_Result],
        application_vnd_vegalite_v5json: typing.Callable[[], T_Result],
        application_vnd_vegalite_v6json: typing.Callable[[], T_Result],
        image_avif: typing.Callable[[], T_Result],
        image_bmp: typing.Callable[[], T_Result],
        image_gif: typing.Callable[[], T_Result],
        image_jpeg: typing.Callable[[], T_Result],
        image_png: typing.Callable[[], T_Result],
        image_svg_xml: typing.Callable[[], T_Result],
        image_tiff: typing.Callable[[], T_Result],
        text_csv: typing.Callable[[], T_Result],
        text_html: typing.Callable[[], T_Result],
        text_latex: typing.Callable[[], T_Result],
        text_markdown: typing.Callable[[], T_Result],
        text_password: typing.Callable[[], T_Result],
        text_plain: typing.Callable[[], T_Result],
        video_mp4: typing.Callable[[], T_Result],
        video_mpeg: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CellOutputMimetype.APPLICATION_JSON:
            return application_json()
        if self is CellOutputMimetype.APPLICATION_VND_JUPYTER_WIDGET_VIEW_JSON:
            return application_vnd_jupyter_widget_view_json()
        if self is CellOutputMimetype.APPLICATION_VND_MARIMO_ERROR:
            return application_vnd_marimo_error()
        if self is CellOutputMimetype.APPLICATION_VND_MARIMO_MIMEBUNDLE:
            return application_vnd_marimo_mimebundle()
        if self is CellOutputMimetype.APPLICATION_VND_MARIMO_TRACEBACK:
            return application_vnd_marimo_traceback()
        if self is CellOutputMimetype.APPLICATION_VND_VEGA_V5JSON:
            return application_vnd_vega_v5json()
        if self is CellOutputMimetype.APPLICATION_VND_VEGA_V6JSON:
            return application_vnd_vega_v6json()
        if self is CellOutputMimetype.APPLICATION_VND_VEGALITE_V5JSON:
            return application_vnd_vegalite_v5json()
        if self is CellOutputMimetype.APPLICATION_VND_VEGALITE_V6JSON:
            return application_vnd_vegalite_v6json()
        if self is CellOutputMimetype.IMAGE_AVIF:
            return image_avif()
        if self is CellOutputMimetype.IMAGE_BMP:
            return image_bmp()
        if self is CellOutputMimetype.IMAGE_GIF:
            return image_gif()
        if self is CellOutputMimetype.IMAGE_JPEG:
            return image_jpeg()
        if self is CellOutputMimetype.IMAGE_PNG:
            return image_png()
        if self is CellOutputMimetype.IMAGE_SVG_XML:
            return image_svg_xml()
        if self is CellOutputMimetype.IMAGE_TIFF:
            return image_tiff()
        if self is CellOutputMimetype.TEXT_CSV:
            return text_csv()
        if self is CellOutputMimetype.TEXT_HTML:
            return text_html()
        if self is CellOutputMimetype.TEXT_LATEX:
            return text_latex()
        if self is CellOutputMimetype.TEXT_MARKDOWN:
            return text_markdown()
        if self is CellOutputMimetype.TEXT_PASSWORD:
            return text_password()
        if self is CellOutputMimetype.TEXT_PLAIN:
            return text_plain()
        if self is CellOutputMimetype.VIDEO_MP4:
            return video_mp4()
        if self is CellOutputMimetype.VIDEO_MPEG:
            return video_mpeg()
