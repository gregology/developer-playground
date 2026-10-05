# Decisions

## 001: Standard library only (2026-10-05)

**Context**: These helpers run inside small scripts on machines where installing packages is slow or not allowed.

**Decision**: The package has no runtime dependencies. Everything uses the Python standard library.

**Rationale**: Installs stay instant, and nothing breaks when a third-party package changes.

**Revisit when**: A feature can't reasonably be built with the standard library.
