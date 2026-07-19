

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingConfigEmbeddingEndpointType(enum.StrEnum):
    """
    The endpoint type for the model.
    """

    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"
    GOOGLE_AI = "google_ai"
    GOOGLE_VERTEX = "google_vertex"
    AZURE = "azure"
    GROQ = "groq"
    OLLAMA = "ollama"
    WEBUI = "webui"
    WEBUI_LEGACY = "webui-legacy"
    LMSTUDIO = "lmstudio"
    LMSTUDIO_LEGACY = "lmstudio-legacy"
    LLAMACPP = "llamacpp"
    KOBOLDCPP = "koboldcpp"
    VLLM = "vllm"
    HUGGING_FACE = "hugging-face"
    MISTRAL = "mistral"
    TOGETHER = "together"
    PINECONE = "pinecone"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        anthropic: typing.Callable[[], T_Result],
        bedrock: typing.Callable[[], T_Result],
        google_ai: typing.Callable[[], T_Result],
        google_vertex: typing.Callable[[], T_Result],
        azure: typing.Callable[[], T_Result],
        groq: typing.Callable[[], T_Result],
        ollama: typing.Callable[[], T_Result],
        webui: typing.Callable[[], T_Result],
        webui_legacy: typing.Callable[[], T_Result],
        lmstudio: typing.Callable[[], T_Result],
        lmstudio_legacy: typing.Callable[[], T_Result],
        llamacpp: typing.Callable[[], T_Result],
        koboldcpp: typing.Callable[[], T_Result],
        vllm: typing.Callable[[], T_Result],
        hugging_face: typing.Callable[[], T_Result],
        mistral: typing.Callable[[], T_Result],
        together: typing.Callable[[], T_Result],
        pinecone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmbeddingConfigEmbeddingEndpointType.OPENAI:
            return openai()
        if self is EmbeddingConfigEmbeddingEndpointType.ANTHROPIC:
            return anthropic()
        if self is EmbeddingConfigEmbeddingEndpointType.BEDROCK:
            return bedrock()
        if self is EmbeddingConfigEmbeddingEndpointType.GOOGLE_AI:
            return google_ai()
        if self is EmbeddingConfigEmbeddingEndpointType.GOOGLE_VERTEX:
            return google_vertex()
        if self is EmbeddingConfigEmbeddingEndpointType.AZURE:
            return azure()
        if self is EmbeddingConfigEmbeddingEndpointType.GROQ:
            return groq()
        if self is EmbeddingConfigEmbeddingEndpointType.OLLAMA:
            return ollama()
        if self is EmbeddingConfigEmbeddingEndpointType.WEBUI:
            return webui()
        if self is EmbeddingConfigEmbeddingEndpointType.WEBUI_LEGACY:
            return webui_legacy()
        if self is EmbeddingConfigEmbeddingEndpointType.LMSTUDIO:
            return lmstudio()
        if self is EmbeddingConfigEmbeddingEndpointType.LMSTUDIO_LEGACY:
            return lmstudio_legacy()
        if self is EmbeddingConfigEmbeddingEndpointType.LLAMACPP:
            return llamacpp()
        if self is EmbeddingConfigEmbeddingEndpointType.KOBOLDCPP:
            return koboldcpp()
        if self is EmbeddingConfigEmbeddingEndpointType.VLLM:
            return vllm()
        if self is EmbeddingConfigEmbeddingEndpointType.HUGGING_FACE:
            return hugging_face()
        if self is EmbeddingConfigEmbeddingEndpointType.MISTRAL:
            return mistral()
        if self is EmbeddingConfigEmbeddingEndpointType.TOGETHER:
            return together()
        if self is EmbeddingConfigEmbeddingEndpointType.PINECONE:
            return pinecone()
