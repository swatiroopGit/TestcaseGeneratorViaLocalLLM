
Write-Host "Initializing Git..."
if (-not (Test-Path .git)) {
    git init
} else {
    Write-Host "Git repo already initialized."
}

Write-Host "Adding files..."
git add .

Write-Host "Committing..."
git commit -m "Initial release: B.L.A.S.T. Architecture v1.0"

Write-Host "Renaming branch to main..."
git branch -M main

Write-Host "Adding remote..."
try {
    git remote add origin https://github.com/swatiroopGit/TestcaseGeneratorViaLocalLLM.git
} catch {
    Write-Host "Remote origin might already exist."
}
# Also try to set url just in case
git remote set-url origin https://github.com/swatiroopGit/TestcaseGeneratorViaLocalLLM.git

Write-Host "Pushing to remote..."
git push -u origin main
