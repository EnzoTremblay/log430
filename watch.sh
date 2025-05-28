#!/bin/bash
ls *.py | entr -r docker compose up --build
