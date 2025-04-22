[Setup]
AppName=Calculator  
AppVersion=1.0  
DefaultDirName={autopf}\Calculator  
DefaultGroupName=Calculator  
OutputDir=.\Output  
OutputBaseFilename=Calculator_Setup  
Compression=lzma  
SolidCompression=yes  

[Files]
Source: "Calculator.exe"; DestDir: "{app}"; Flags: ignoreversion  

[Icons]
; App shortcut
Name: "{group}\Calculator"; Filename: "{app}\Calculator.exe"  
; Desktop shortcut (optional)
Name: "{commondesktop}\Calculator"; Filename: "{app}\Calculator.exe"  
; Uninstaller shortcut (added to Start Menu)
Name: "{group}\Uninstall Calculator"; Filename: "{uninstallexe}"  
[UninstallDelete]
Type: files; Name: "{app}\Calculator.exe"
