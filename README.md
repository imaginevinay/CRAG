# Corrective RAG (CRAG)

A production-ready Retrieval-Augmented Generation (RAG) system that intelligently routes queries, validates document relevance, detects hallucinations, and gracefully falls back to web search when needed.

## What It Does

CRAG implements a sophisticated multi-step workflow that:

1. **Routes Queries** - Intelligently directs questions to either web search or vector store retrieval
2. **Retrieves Documents** - Fetches relevant documents from a ChromaDB vector store
3. **Grades Relevance** - Evaluates retrieved documents for relevance to the query
4. **Generates Answers** - Creates responses using retrieved documents
5. **Detects Hallucinations** - Validates that answers are grounded in source documents
6. **Validates Accuracy** - Ensures answers actually address the user's question
7. **Fallback Search** - Automatically performs web search if documents aren't relevant

## Architecture

![CRAG Flow Diagram](graph.png)

The workflow uses a state-based graph architecture built with LangGraph, enabling dynamic routing and conditional execution paths.

## Tech Stack

- **LangChain** - LLM orchestration and document processing
- **LangGraph** - Agentic graph-based workflows
- **ChromaDB** - Vector database for document storage and retrieval
- **Ollama** - Local embeddings model (qwen2:1.5b)
- **Tavily** - Web search integration
- **Google GenAI** - LLM backend
- **Python 3.11+** - Runtime

## Getting Started

### Prerequisites

- Python 3.11 or higher
- [Ollama](https://ollama.ai) installed with `qwen2:1.5b` model
- `.env` file with required API keys

### Setup

1. Clone the repository
   ```bash
   git clone <repo-url>
   cd rag
   ```

2. Create `.env` file (copy from `.env.example`):
   ```bash
   GOOGLE_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
   LANGSMITH_API_KEY=your_key_here  # Optional: for tracing
   ```

3. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

4. Ingest documents into vector store:
   ```bash
   uv run ingestion.py
   ```

5. Run the application:
   ```bash
   uv run main.py
   ```

## Tracing with LangSmith

To trace your workflows in LangSmith:

1. Get your API key from [LangSmith](https://smith.langchain.com)

2. Add to `.env`:
   ```
   LANGSMITH_API_KEY=your_api_key
   LANGSMITH_PROJECT=crag-project
   ```

3. LangGraph and LangChain operations will automatically be traced. View traces at:
   ```
   https://smith.langchain.com/projects/crag-project
   ```

This provides full visibility into:
- LLM calls and responses
- Retrieved documents
- Grading decisions
- Web search queries
- Generation quality metrics

## Project Structure

```
rag/
├── graph/               # Core CRAG workflow
│   ├── state.py        # GraphState definition
│   ├── graph.py        # Graph construction
│   ├── consts.py       # Constants
│   ├── chains/         # LLM chains for each task
│   │   ├── router.py
│   │   ├── answer_grader.py
│   │   ├── hallucination_grader.py
│   │   └── ...
│   └── nodes/          # Graph execution nodes
│       ├── retrieve.py
│       ├── generate.py
│       └── ...
├── ingestion.py        # Vector store population
├── main.py             # Application entry point
└── pyproject.toml      # Dependencies
```

## License

MIT
