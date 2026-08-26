Add-AppxPackage -AppInstallerFile https://cdn.files.community/files/stable/Files.Package.appinstaller
Add-AppxPackage -AppInstallerFile https://cdn.files.community/files/preview/Files.Package.appinstaller
winget install -e --id FilesCommunity.Files
winget install -e --id FilesCommunity.FilesPreview
scoop install nonportable/files-np
choco install files
scoop install nonportable/files-preview-np
