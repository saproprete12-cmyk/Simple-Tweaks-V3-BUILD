#define MyAppName "Simple Tweaks V3"
#define MyAppVersion "3.0.0"
#define MyAppPublisher "Simple Tweaks"
#define MyAppExeName "SimpleTweaks.exe"

[Setup]
AppId={{9F77A120-3B27-4D83-8F7A-4B2A0D3E7C91}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\Simple Tweaks V3
DefaultGroupName={#MyAppName}
OutputDir=installer_output
OutputBaseFilename=SimpleTweaks_Setup_V3
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesInstallIn64BitMode=x64
UninstallDisplayIcon={app}\{#MyAppExeName}

[Files]
Source: "dist\SimpleTweaks.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Simple Tweaks V3"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\Simple Tweaks V3"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Créer un raccourci sur le Bureau"; GroupDescription: "Raccourcis supplémentaires :"; Flags: unchecked

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Lancer Simple Tweaks V3"; Flags: postinstall nowait skipifsilent
