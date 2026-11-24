$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$projectRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$scenes = Get-Content (Join-Path $PSScriptRoot 'cenas.json') -Raw -Encoding utf8 | ConvertFrom-Json
$voiceOutput = Join-Path $projectRoot 'output\video_inicial\audio'
$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speaker.SelectVoice('Microsoft Maria Desktop')
$speaker.Rate = 1
$speaker.Volume = 100
foreach ($scene in $scenes) {
    $fileName = 'voz_{0:00}.wav' -f $scene.id
    $speaker.SetOutputToWaveFile((Join-Path $voiceOutput $fileName))
    $speaker.Speak($scene.voice)
    $speaker.SetOutputToNull()
    Write-Output $fileName
}
$speaker.Dispose()
