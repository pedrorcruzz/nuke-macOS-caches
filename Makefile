.PHONY: run

GO = go

run:
	@bash -c '$(GO) run main.go 2>/dev/null || true'
