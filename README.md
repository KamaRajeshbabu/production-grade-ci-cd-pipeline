# Production-Grade CI/CD Pipeline

![CI Pipeline](https://github.com/KamaRajeshbabu/production-grade-ci-cd-pipeline/actions/workflows/ci.yml/badge.svg)

## Overview
This project demonstrates a production-style CI/CD pipeline using GitHub Actions for automated testing, Docker builds, and artifact management.

## Features
- Triggered on push and pull requests
- Automated test validation using pytest
- Failure detection to block faulty builds
- Docker image build for deployment
- Artifact storage for reproducibility

## Workflow Stages
1. Code checkout
2. Dependency installation
3. Test execution
4. Docker build
5. Artifact upload

## Tech Stack
- Python
- FastAPI
- GitHub Actions
- Docker
- Pytest

## Outcome
Ensures reliable, repeatable build and deployment workflows while reducing manual validation effort.
