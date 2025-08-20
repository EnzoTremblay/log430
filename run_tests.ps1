Param(
    [string]$Pattern = "test_*.py"
)

Write-Host "Running Lab 2 tests..." -ForegroundColor Cyan
& "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" -m unittest discover -s lab/lab2/src -p $Pattern -v

Write-Host "Running Lab 3 tests..." -ForegroundColor Cyan
& "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" -m unittest -v lab.lab3.test_api

Write-Host "Running Lab 4 tests..." -ForegroundColor Cyan
& "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" -m unittest -v lab.lab4.test_api

Write-Host "Running Lab 5 service tests..." -ForegroundColor Cyan
& "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" -m unittest discover -s lab/lab5/tests -p $Pattern -v

Write-Host "Running Lab 6 tests..." -ForegroundColor Cyan
& "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" -m unittest -v lab.lab6.tests.test_saga
