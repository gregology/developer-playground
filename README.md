# developer-playground

A throwaway repository for exercising [Developer](https://github.com/gregology/developer) pipelines end to end. Issues and pull requests here are seeded on purpose; some code contains deliberate bugs.

## Development

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
```
