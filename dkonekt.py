import fire
import os
#Сборка + установка пакета
def install(package):
	if package=="xpomocomcalc":
		print("License = Bsd 2 clause")
		print("Getting xpomocomcalc...")
		os.system("git clone https://github.com/justcoding13/calc_hromosom.git /etc/diakonekt/temp")
		print("Building xpomocomcalc...")
		os.system("cd /etc/diakonekt/temp/1.2; make")
		print("Installing xpomocomcalc...")
		os.system("cd /etc/diakonekt/temp/1.2; sudo mv -v calcxpom /usr/bin")
		print("xpomocomcalc was installed!")
	else:
		print("Error: Unknown konekt")
#Удаления мусора
def clean():
	os.system("sudo rm -Rv /etc/diakonekt/temp")
	os.system("mkdir -v /etc/diakonekt/temp")
#Удаление пакета
def remove(package):
	if package=="xpomocomcalc":
		print("Removing xpomocomcalc...")
		os.system("sudo rm -v /usr/bin/calcxpom")
		print("xpomocomcalc was removed!")
	else:
		print("Error: Unknown konekt")
if __name__ == '__main__':
    fire.Fire()
