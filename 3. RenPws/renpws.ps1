# Fonction pour relancer le script en tant qu'administrateur si nécessaire
function Ensure-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    if (-not $currentUser.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        $newProcess = New-Object System.Diagnostics.ProcessStartInfo "PowerShell";
        $newProcess.Arguments = "& '" + $script:MyInvocation.MyCommand.Path + "'"
        $newProcess.Verb = "runas"
        [System.Diagnostics.Process]::Start($newProcess)
        exit
    }
}

# Vérifier et demander les droits d'administrateur si nécessaire
Ensure-Admin

# Importation du module pour les interfaces graphiques
Add-Type -AssemblyName PresentationFramework

# Création de la fenêtre
[void][System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms')
[void][System.Reflection.Assembly]::LoadWithPartialName('System.Drawing')

$form = New-Object System.Windows.Forms.Form
$form.Text = "Renommer l'ordinateur"
$form.Size = New-Object System.Drawing.Size(450,200)
$form.StartPosition = "CenterScreen"

# Définir la police
$font = New-Object System.Drawing.Font("Microsoft Sans Serif", 10, [System.Drawing.FontStyle]::Bold)

# Création des labels et des champs de saisie
$label1 = New-Object System.Windows.Forms.Label
$label1.Text = "Type (UC/PORT):"
$label1.Size = New-Object System.Drawing.Size(200,20)
$label1.Location = New-Object System.Drawing.Point(10,20)
$label1.Font = $font
$form.Controls.Add($label1)

$combobox = New-Object System.Windows.Forms.ComboBox
$combobox.Items.Add("UC")
$combobox.Items.Add("PORT")
$combobox.DropDownStyle = [System.Windows.Forms.ComboBoxStyle]::DropDownList
$combobox.Size = New-Object System.Drawing.Size(200,20)
$combobox.Location = New-Object System.Drawing.Point(220,20)
$combobox.Font = $font
$form.Controls.Add($combobox)

$label2 = New-Object System.Windows.Forms.Label
$label2.Text = "Nom du service:"
$label2.Size = New-Object System.Drawing.Size(200,20)
$label2.Location = New-Object System.Drawing.Point(10,60)
$label2.Font = $font
$form.Controls.Add($label2)

$serviceBox = New-Object System.Windows.Forms.TextBox
$serviceBox.Size = New-Object System.Drawing.Size(200,20)
$serviceBox.Location = New-Object System.Drawing.Point(220,60)
$serviceBox.Font = $font
$form.Controls.Add($serviceBox)

# Bouton pour renommer l'ordinateur
$buttonOK = New-Object System.Windows.Forms.Button
$buttonOK.Text = "Renommer"
$buttonOK.Size = New-Object System.Drawing.Size(100,30)
$buttonOK.Location = New-Object System.Drawing.Point(150,100)
$buttonOK.Font = $font
$form.Controls.Add($buttonOK)

# Définir les couleurs pour le mode sombre
$darkBackColor = [System.Drawing.ColorTranslator]::FromHtml("#454545")
$darkForeColor = [System.Drawing.Color]::White

# Appliquer le mode sombre
$form.BackColor = $darkBackColor
$label1.ForeColor = $darkForeColor
$label2.ForeColor = $darkForeColor
$combobox.BackColor = $darkBackColor
$combobox.ForeColor = $darkForeColor
$serviceBox.BackColor = $darkBackColor
$serviceBox.ForeColor = $darkForeColor
$buttonOK.BackColor = $darkBackColor
$buttonOK.ForeColor = $darkForeColor

# Action du bouton pour renommer l'ordinateur
$buttonOK.Add_Click({
    $prefix = $combobox.SelectedItem
    $service = $serviceBox.Text
    $date = Get-Date -Format "yyMM"
    $newName = "$prefix$date-$service"
    
    # Renommage de l'ordinateur
    Rename-Computer -NewName $newName -Force -Restart
})

# Affichage de la fenêtre
$form.Topmost = $true
$form.Add_Shown({$form.Activate()})
[void] $form.ShowDialog()
