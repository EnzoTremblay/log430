# Stop Flask dev servers listening on the default lab ports
$ports = @(5202, 5203, 5001, 5002, 5003, 5004, 5005, 5006)
$net = netstat -ano | Select-String -Pattern ($ports -join "|")
$net | ForEach-Object {
  $pid = ($_ -split "\s+")[-1]
  if ($pid -match "^\d+$") {
    try { Stop-Process -Id [int]$pid -Force -ErrorAction Stop } catch {}
  }
}
Write-Host "Stopped lab processes on ports: $($ports -join ', ')" -ForegroundColor Yellow
