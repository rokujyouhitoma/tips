MAIN_CLASS_NAME=HelloWorld

.PHONY: help
help: ## help command
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## clean
	rm *.class

.PHONY: run
run: ## run
	java ${MAIN_CLASS_NAME}

.PHONY: compile
compile: ## javac compile
	javac *.java
