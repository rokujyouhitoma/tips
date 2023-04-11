THIRD_DIR=third
MAIN_CLASS_NAME=ScriptEngineExample
CLASS_PATH=third/rhino-1.7.14.jar:third/rhino-engine-1.7.14.jar

.PHONY: help
help: ## help command
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## clean
	rm *.class

.PHONY: setup
setup: ## setup
	cd $(THIRD_DIR) && curl -OL https://github.com/mozilla/rhino/releases/download/Rhino1_7_14_Release/rhino-1.7.14.jar
	cd $(THIRD_DIR) && curl -OL https://github.com/mozilla/rhino/releases/download/Rhino1_7_14_Release/rhino-engine-1.7.14.jar

.PHONY: run
run: ## run
	java -classpath .:${CLASS_PATH} ${MAIN_CLASS_NAME}

.PHONY: compile
compile: ## javac compile
	javac -classpath .:${CLASS_PATH} ${MAIN_CLASS_NAME}.java
