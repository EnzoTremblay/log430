Param(
  [string]$BaseDir = (Get-Location)
)

$ErrorActionPreference = 'Stop'

function Test-Endpoint {
  param(
    [string]$Name,
    [string]$Method = 'GET',
    [string]$Url,
    [string]$Body = $null
  )
  Write-Host "- $Name => $Url" -ForegroundColor Cyan
  try {
    if ($Method -eq 'GET') {
      $resp = Invoke-WebRequest -Uri $Url -UseBasicParsing -Method GET -TimeoutSec 5
    } elseif ($Method -eq 'PUT') {
      $resp = Invoke-WebRequest -Uri $Url -UseBasicParsing -Method PUT -ContentType 'application/json' -Body $Body -TimeoutSec 5
    } elseif ($Method -eq 'POST') {
      $resp = Invoke-WebRequest -Uri $Url -UseBasicParsing -Method POST -ContentType 'application/json' -Body $Body -TimeoutSec 5
    } else {
      throw "Unsupported method $Method"
    }
    Write-Host "  OK ($($resp.StatusCode))" -ForegroundColor Green
  }
  catch {
    Write-Host "  FAIL: $($_.Exception.Message)" -ForegroundColor Red
    throw
  }
}

Write-Host "Lab 2" -ForegroundColor Yellow
Test-Endpoint -Name 'L2 stock' -Url 'http://localhost:5202/api/v1/stores/1/stock'
Test-Endpoint -Name 'L2 rapport' -Url 'http://localhost:5202/api/v1/report'
Test-Endpoint -Name 'L2 update prod 1' -Method PUT -Url 'http://localhost:5202/api/v1/products/1' -Body '{"prix": 19.99, "stock": 50}'
Test-Endpoint -Name 'L2 dashboard' -Url 'http://localhost:5202/api/v1/dashboard'

Write-Host "Lab 3" -ForegroundColor Yellow
Test-Endpoint -Name 'L3 stock' -Url 'http://localhost:5203/api/v1/stores/1/stock'
Test-Endpoint -Name 'L3 rapport' -Url 'http://localhost:5203/api/v1/report'
Test-Endpoint -Name 'L3 update prod 1' -Method PUT -Url 'http://localhost:5203/api/v1/products/1' -Body '{"prix": 21.5, "stock": 40}'
Test-Endpoint -Name 'L3 dashboard' -Url 'http://localhost:5203/api/v1/dashboard'

Write-Host "Lab 5" -ForegroundColor Yellow
Test-Endpoint -Name 'Produits list' -Url 'http://localhost:5001/api/v1/products'
Test-Endpoint -Name 'Ventes list' -Url 'http://localhost:5002/api/v1/sales'
Test-Endpoint -Name 'Stock list' -Url 'http://localhost:5003/api/v1/stock'
Test-Endpoint -Name 'Clients create' -Method POST -Url 'http://localhost:5004/api/v1/clients' -Body '{"nom":"Alice"}'
Test-Endpoint -Name 'Panier create' -Method POST -Url 'http://localhost:5005/api/v1/cart' -Body '{"client_id":1, "produits":[1,2]}'
Test-Endpoint -Name 'Commande checkout' -Method POST -Url 'http://localhost:5006/api/v1/checkout' -Body '{"client_id":1, "panier_id":1}'

Write-Host "All smoke tests passed." -ForegroundColor Green
