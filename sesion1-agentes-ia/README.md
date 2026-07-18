# Agentes de IA, Orquestación y Protocolos — Notebooks de la Sesión 1

Notebooks prácticos del curso de IA aplicada para equipos de desarrollo, correspondientes a la **Sesión 1**: Agentes de IA, LangChain/LlamaIndex, MCP y Function Calling.

Cada notebook es **independiente** (instala solo las dependencias que necesita) y están ordenados por complejidad creciente. Disponibles en dos versiones equivalentes, según el proveedor de LLM que quieras usar:

- **[`/anthropic`](./anthropic)** — usando la API de Claude (Anthropic).
- **[`/gemini`](./gemini)** — usando la API de Gemini (Google), con la Interactions API vigente en 2026.

## Notebooks

| Notebook | Dependencias | Complejidad |
|---|---|---|
| `function_calling_tool_use` | SDK del proveedor únicamente | 🟢 Básica |
| `agente_react_manual` | SDK del proveedor únicamente | 🟢 Básica |
| `langchain_agente` | + `langchain` | 🟡 Media |
| `llamaindex_rag` | + `llama-index` | 🟡 Media-alta |
| `mcp_servidor_cliente` | + `mcp`, `nest_asyncio` | 🟠 Alta |
| `taller5_prototipo_agente` | SDK del proveedor únicamente (plantilla del taller) | 🟢 Básica para empezar |

Cada notebook incluye:
- 🎯 **Objetivo de aprendizaje** — qué vas a poder hacer al terminarlo.
- 📚 **Teoría** — el concepto explicado antes de tocar código.
- Ejercicio(s) práctico(s) al final para reforzar lo aprendido.

## Cómo usarlos

1. Abre el notebook que te interese directamente en Google Colab (botón "Open in Colab" si lo agregas, o `File > Upload notebook` desde Colab).
2. Cada notebook te pide su propia API key la primera vez que lo corres:
   - **Anthropic**: [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)
   - **Gemini**: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
3. Ejecuta las celdas en orden. Los notebooks son autocontenidos — no dependen de haber corrido otro antes (excepto el de Taller 5, que reutiliza el mismo patrón de código del notebook `agente_react_manual`, pero copiado, no importado).

## Nota sobre Gemini y las API keys "AQ."

Al momento de escribir estos notebooks, Google está migrando las API keys al nuevo formato con prefijo `AQ.` (antes `AIza...`). Existen reportes activos en el foro oficial de Google de que estas keys devuelven `401 ACCESS_TOKEN_TYPE_UNSUPPORTED` en algunas cuentas, incluso bien configuradas. Los notebooks de `/gemini` incluyen una celda de diagnóstico que te avisa si tu key tiene ese formato.

## Estructura del repositorio

```
.
├── anthropic/
│   ├── function_calling_tool_use.ipynb
│   ├── agente_react_manual.ipynb
│   ├── langchain_agente.ipynb
│   ├── llamaindex_rag.ipynb
│   ├── mcp_servidor_cliente.ipynb
│   └── taller5_prototipo_agente.ipynb
└── gemini/
    ├── function_calling_tool_use_gemini.ipynb
    ├── agente_react_manual_gemini.ipynb
    ├── langchain_agente_gemini.ipynb
    ├── llamaindex_rag_gemini.ipynb
    ├── mcp_servidor_cliente_gemini.ipynb
    └── taller5_prototipo_agente_gemini.ipynb
```
