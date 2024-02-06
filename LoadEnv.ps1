$envPath = ".\.env" # Adjust the path to your .env file if necessary
Get-Content $envPath | ForEach-Object {
    $line = $_.Trim()
    if (-not [string]::IsNullOrWhiteSpace($line) -and -not $line.StartsWith("#")) {
        $keyValue = $line -split '=', 2
        [System.Environment]::SetEnvironmentVariable($keyValue[0], $keyValue[1], [System.EnvironmentVariableTarget]::Process)
    }
}
