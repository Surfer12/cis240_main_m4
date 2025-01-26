param(
    [switch]$WhatIf = $false
)

# Function to rename files recursively
function Rename-FilesWithUnderscores {
    param(
        [string]$Path
    )

    Get-ChildItem -Path $Path -Recurse | ForEach-Object {
        if ($_.Name -match '-') {
            $newName = $_.Name -replace '-', '_'
            
            if ($_.PSIsContainer) {
                # For directories
                $newFullPath = Join-Path -Path $_.Parent.FullName -ChildPath $newName
                
                if ($WhatIf) {
                    Write-Host "Would rename directory: $($_.FullName) to $newFullPath"
                }
                else {
                    Rename-Item -Path $_.FullName -NewName $newName -ErrorAction Continue
                    Write-Host "Renamed directory: $($_.FullName) to $newFullPath"
                }
            }
            else {
                # For files
                $newFullPath = Join-Path -Path $_.DirectoryName -ChildPath $newName
                
                if ($WhatIf) {
                    Write-Host "Would rename file: $($_.FullName) to $newFullPath"
                }
                else {
                    Rename-Item -Path $_.FullName -NewName $newName -ErrorAction Continue
                    Write-Host "Renamed file: $($_.FullName) to $newFullPath"
                }
            }
        }
    }
}

# Run the renaming function
Rename-FilesWithUnderscores -Path "."

# Optional: If you want to do a dry run first, use the script with -WhatIf
# .\rename_files.ps1 -WhatIf 