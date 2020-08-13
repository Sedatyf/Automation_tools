import os, glob
import tqdm

file_folder = input("Veuillez spécifier le chemin du dossier à scanner : ")
file_extension = input("Veuillez spécifier l'extension des fichiers : ")
chars_to_replace = input("Veuillez préciser les caractères à remplacer : ")
chars_replaced_by = input("Par quels caractères seront-ils remplacer ? ")

file_list = []
new_lines = []

def main():
    for root, dirs, files in os.walk(file_folder):
        for current_file in files:
            if current_file.endswith(file_extension):
                file_list.append(os.path.join(root, current_file))

    pbar_change_chars = tqdm.tqdm(file_list)
    for current_file in pbar_change_chars:
        pbar_change_chars.set_description("Modification des fichiers")
        with open(current_file, "r", encoding="ISO-8859-1") as open_file:
            old_lines = open_file.readlines()
        path_to_file = os.path.join(file_folder,current_file)
        f = open(path_to_file, "w")
        for line in old_lines:
            f.write(line.replace(chars_to_replace, chars_replaced_by))
        f.close()
    os.system("pause")

if __name__ == "__main__":
    main()
