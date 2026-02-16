#define AppName "cochavim_uzmanim_plus"

[Setup]
AppName={#AppName}
AppVersion=1.0
DefaultDirName={commonpf}\{#AppName}
OutputBaseFilename={#AppName}
Compression=lzma
SolidCompression=yes
CreateAppDir=yes
DisableProgramGroupPage=no
DefaultGroupName={#AppName}
SetupIconFile=cu_icon.ico

[Languages]
Name: "hebrew"; MessagesFile: "compiler:Languages\Hebrew.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "cochavim_uzmanim_plus_dir\cochavim_uzmanim_plus_dir.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "cochavim_uzmanim_plus_dir\_internal\*"; DestDir: "{app}\_internal"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{commondesktop}\{#AppName}"; Filename: "{app}\cochavim_uzmanim_plus_dir.exe"
Name: "{group}\{#AppName}"; Filename: "{app}\cochavim_uzmanim_plus_dir.exe"

[Run]
Filename: "{app}\cochavim_uzmanim_plus_dir.exe"; Description: "Run {#AppName}"; Flags: nowait postinstall skipifsilent

