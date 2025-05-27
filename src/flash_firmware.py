import subprocess
import os
import platform

# Détecter le système d'exploitation
system_os = platform.system()

# Chemin vers l'exécutable avrdude pour chaque OS
if system_os == 'Windows':
    avrdude_exe = os.path.join(os.getcwd(), 'avrdude', 'avrdude.exe')
elif system_os == 'Darwin':  # macOS
    avrdude_exe = os.path.join(os.getcwd(), 'avrdude', 'avrdude')
else:  # Linux
    avrdude_exe = os.path.join(os.getcwd(), 'avrdude', 'avrdude')

def flash_firmware(hex_file_path, port, microcontroller_type="m328p"):
    avrdude_cmd = [
        avrdude_exe,
        "-v",                    # Verbose
        "-p", microcontroller_type,  # Type de microcontrôleur (m328p pour Arduino Uno)
        "-c", "arduino",          # Type de programmateur (Arduino)
        "-P", port,               # Port série (ex : COM3 sur Windows, /dev/ttyUSB0 sur Linux/Mac)
        "-b", "115200",           # Vitesse de communication (115200 baud)
        "-D",                    # Désactivation de la lecture de la mémoire
        "-U", f"flash:w:{hex_file_path}:i"  # Flashage du fichier .hex
    ]

    try:
        subprocess.run(avrdude_cmd, check=True)
        print("Firmware flashé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du flashage : {e}")
    except FileNotFoundError:
        print("avrdude n'est pas trouvé. Assurez-vous qu'il est dans le dossier du projet.")

# Exemple d'utilisation
if __name__ == "__main__":
    hex_file = "path/to/Pedro.hex"  # Remplace avec le chemin de ton fichier .hex
    port = "/dev/ttyUSB0"  # Exemple pour Linux/Mac
    flash_firmware(hex_file, port)
