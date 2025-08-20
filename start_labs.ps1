Param(
  [string]$PythonExe = "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe"
)

Write-Host "Starting Lab 2 on http://localhost:5202" -ForegroundColor Cyan
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command `$env:PORT='5202'; & '$PythonExe' lab/lab2/src/api.py"

Write-Host "Starting Lab 3 on http://localhost:5203" -ForegroundColor Cyan
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command `$env:PYTHONPATH='$(Get-Location)'; `$env:PORT='5203'; & '$PythonExe' lab/lab3/api.py"

Write-Host "Starting Lab 5 services on ports 5001..5006" -ForegroundColor Cyan
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command & '$PythonExe' lab/lab5/services/produits.py"
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command & '$PythonExe' lab/lab5/services/ventes.py"
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command & '$PythonExe' lab/lab5/services/stock.py"
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command & '$PythonExe' lab/lab5/services/clients.py"
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command & '$PythonExe' lab/lab5/services/panier.py"
Start-Process -WindowStyle Minimized powershell -ArgumentList "-NoExit -Command & '$PythonExe' lab/lab5/services/commande.py"

Write-Host "All labs started in separate windows. Press Ctrl+C to stop here or run stop_labs.ps1 to free ports." -ForegroundColor Green
