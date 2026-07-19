

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LlmConfigModelEndpointType(enum.StrEnum):
    """
    The endpoint type for the model.
    """

    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE_AI = "google_ai"
    GOOGLE_VERTEX = "google_vertex"
    AZURE = "azure"
    GROQ = "groq"
    OLLAMA = "ollama"
    WEBUI = "webui"
    WEBUI_LEGACY = "webui-legacy"
    LMSTUDIO = "lmstudio"
    LMSTUDIO_LEGACY = "lmstudio-legacy"
    LMSTUDIO_CHATCOMPLETIONS = "lmstudio-chatcompletions"
    LLAMACPP = "llamacpp"
    KOBOLDCPP = "koboldcpp"
    VLLM = "vllm"
    HUGGING_FACE = "hugging-face"
    MISTRAL = "mistral"
    TOGETHER = "together"
    BEDROCK = "bedrock"
    DEEPSEEK = "deepseek"
    XAI = "xai"
    ZAI = "zai"
    CHATGPT_OAUTH = "chatgpt_oauth"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        anthropic: typing.Callable[[], T_Result],
        google_ai: typing.Callable[[], T_Result],
        google_vertex: typing.Callable[[], T_Result],
        azure: typing.Callable[[], T_Result],
        groq: typing.Callable[[], T_Result],
        ollama: typing.Callable[[], T_Result],
        webui: typing.Callable[[], T_Result],
        webui_legacy: typing.Callable[[], T_Result],
        lmstudio: typing.Callable[[], T_Result],
        lmstudio_legacy: typing.Callable[[], T_Result],
        lmstudio_chatcompletions: typing.Callable[[], T_Result],
        llamacpp: typing.Callable[[], T_Result],
        koboldcpp: typing.Callable[[], T_Result],
        vllm: typing.Callable[[], T_Result],
        hugging_face: typing.Callable[[], T_Result],
        mistral: typing.Callable[[], T_Result],
        together: typing.Callable[[], T_Result],
        bedrock: typing.Callable[[], T_Result],
        deepseek: typing.Callable[[], T_Result],
        xai: typing.Callable[[], T_Result],
        zai: typing.Callable[[], T_Result],
        chatgpt_oauth: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmConfigModelEndpointType.OPENAI:
            return openai()
        if self is LlmConfigModelEndpointType.ANTHROPIC:
            return anthropic()
        if self is LlmConfigModelEndpointType.GOOGLE_AI:
            return google_ai()
        if self is LlmConfigModelEndpointType.GOOGLE_VERTEX:
            return google_vertex()
        if self is LlmConfigModelEndpointType.AZURE:
            return azure()
        if self is LlmConfigModelEndpointType.GROQ:
            return groq()
        if self is LlmConfigModelEndpointType.OLLAMA:
            return ollama()
        if self is LlmConfigModelEndpointType.WEBUI:
            return webui()
        if self is LlmConfigModelEndpointType.WEBUI_LEGACY:
            return webui_legacy()
        if self is LlmConfigModelEndpointType.LMSTUDIO:
            return lmstudio()
        if self is LlmConfigModelEndpointType.LMSTUDIO_LEGACY:
            return lmstudio_legacy()
        if self is LlmConfigModelEndpointType.LMSTUDIO_CHATCOMPLETIONS:
            return lmstudio_chatcompletions()
        if self is LlmConfigModelEndpointType.LLAMACPP:
            return llamacpp()
        if self is LlmConfigModelEndpointType.KOBOLDCPP:
            return koboldcpp()
        if self is LlmConfigModelEndpointType.VLLM:
            return vllm()
        if self is LlmConfigModelEndpointType.HUGGING_FACE:
            return hugging_face()
        if self is LlmConfigModelEndpointType.MISTRAL:
            return mistral()
        if self is LlmConfigModelEndpointType.TOGETHER:
            return together()
        if self is LlmConfigModelEndpointType.BEDROCK:
            return bedrock()
        if self is LlmConfigModelEndpointType.DEEPSEEK:
            return deepseek()
        if self is LlmConfigModelEndpointType.XAI:
            return xai()
        if self is LlmConfigModelEndpointType.ZAI:
            return zai()
        if self is LlmConfigModelEndpointType.CHATGPT_OAUTH:
            return chatgpt_oauth()
