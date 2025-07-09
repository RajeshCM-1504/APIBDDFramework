#!/bin/bash
cd "$(dirname "$0")"
rm -rf allure-results
mkdir -p allure-results
behave --no-capture -t @regression -f allure_behave.formatter:AllureFormatter -o allure-results