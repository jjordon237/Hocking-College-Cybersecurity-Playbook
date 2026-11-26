# NET2220 Milestone 1 Windows baseline
# Setup commands collated from the recorded lab work and course instructions.
# Initial build on a fresh course server, using Windows PowerShell as Administrator.
# Accounts and groups already exist on the current course server.
# This file is not a rollback script and has not been run as a complete script.

# Create the local role groups.
New-LocalGroup -Name "M1-Readers"
New-LocalGroup -Name "M1-Operators"

# Request the lab test password interactively; no password value is stored here.
$pw = Read-Host -AsSecureString "Test password"

# Create the three local test accounts.
New-LocalUser -Name "m1reader" -Password $pw
New-LocalUser -Name "m1operator" -Password $pw
New-LocalUser -Name "m1retired" -Password $pw

# Assign the role groups and built-in Users membership.
Add-LocalGroupMember -Group "M1-Readers" -Member "m1reader","m1operator"
Add-LocalGroupMember -Group "M1-Operators" -Member "m1operator"
Add-LocalGroupMember -Group "Users" -Member "m1reader","m1operator","m1retired"

# Disable the retired account.
Disable-LocalUser -Name "m1retired"

# Create the course folders and the published notice.
New-Item -ItemType Directory C:\CourseLab\Published, C:\CourseLab\Working
Set-Content C:\CourseLab\Published\notice.txt 'Team Notice'

# Set the course folder permissions and remove inherited access entries.
icacls C:\CourseLab\Published /inheritance:r /grant "Administrators:(OI)(CI)F" "SYSTEM:(OI)(CI)F" "M1-Readers:(OI)(CI)RX"
icacls C:\CourseLab\Working /inheritance:r /grant "Administrators:(OI)(CI)F" "SYSTEM:(OI)(CI)F" "M1-Operators:(OI)(CI)M"

# Recorded read-only verification commands.
whoami; hostname; Get-Date
icacls C:\CourseLab\Published
icacls C:\CourseLab\Working
Get-LocalUser -Name m1reader,m1operator,m1retired | Select-Object Name,Enabled
Get-LocalGroupMember -Group "M1-Readers" | Select-Object Name
Get-LocalGroupMember -Group "M1-Operators" | Select-Object Name
Get-LocalGroupMember -Group "Administrators" | Select-Object Name
