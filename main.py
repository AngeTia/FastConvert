import os
import ffmpeg
import tkinter as tk
from tkinter import filedialog

# Fonction pour convertir le fichier MP4 en MP3
def convert_mp4_to_mp3(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file, acodec='libmp3lame').run()
        result_label.config(text=f"Conversion réussie: {output_file}")
    except ffmpeg.Error as e:
        result_label.config(text=f"Erreur lors de la conversion : {e}")

# Fonction pour parcourir et sélectionner un fichier MP4
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers MP4", "*.mp4")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

# Fonction pour parcourir et sélectionner un dossier de sortie
def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_folder)

# Fonction pour démarrer la conversion
def convert():
    input_file = input_entry.get()
    output_folder = output_entry.get()
    output_file = os.path.join(output_folder, "output.mp3")
    convert_mp4_to_mp3(input_file, output_file)

# Créer une fenêtre principale pour l'interface graphique
app = tk.Tk()
app.title("FastConvert By @AngeTia")

# Entry pour le fichier d'entrée
input_entry = tk.Entry(app, width=50)
input_entry.grid(row=0, column=0, padx=10, pady=5)

# Bouton pour parcourir le fichier
browse_button = tk.Button(app, text="Parcourir", command=browse_file)
browse_button.grid(row=0, column=1, padx=5, pady=5)

# Entry pour le dossier de sortie
output_entry = tk.Entry(app, width=50)
output_entry.grid(row=1, column=0, padx=10, pady=5)

# Bouton pour parcourir le dossier de sortie
browse_output_button = tk.Button(app, text="Dossier de sortie", command=browse_output_folder)
browse_output_button.grid(row=1, column=1, padx=5, pady=5)

# Bouton de conversion
convert_button = tk.Button(app, text="Convertir en MP3", command=convert)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Label pour afficher le résultat de la conversion
result_label = tk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

app.mainloop()
