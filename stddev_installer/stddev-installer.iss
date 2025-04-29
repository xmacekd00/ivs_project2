; -- stddev_installer.iss --
[Setup]
AppName=StdDev
AppVersion=1.0
DefaultDirName={autopf}\StdDev
DefaultGroupName=StdDev
UninstallDisplayIcon={app}\stddev.exe
Compression=lzma2
SolidCompression=yes
OutputDir=.\Output
OutputBaseFilename=StdDev_Setup

[Files]
; Main executable
Source: "stddev.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Start Menu shortcuts
Name: "{group}\StdDev"; Filename: "{app}\stddev.exe"
Name: "{group}\Uninstall StdDev"; Filename: "{uninstallexe}"
; Optional desktop shortcut
Name: "{commondesktop}\StdDev"; Filename: "{app}\stddev.exe"
