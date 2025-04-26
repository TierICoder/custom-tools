[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$player = New-Object System.Media.SoundPlayer "E:\Genel_Dosyalar\RefugeoftheSurvivors.wav"
$player.PlayLooping()

Start-Job -ScriptBlock $playMusic


Add-Type -AssemblyName PresentationFramework
[System.Windows.MessageBox]::Show("Canını sıkma, moralini bozma. Eğer hâlâ nefes alıyorsan mücadeleye devam etmelisin 💪", "Yeni Bir Gün")